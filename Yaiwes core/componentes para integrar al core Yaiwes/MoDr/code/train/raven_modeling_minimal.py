"""Minimal modeling.py file for HF compatibility and funny zero-shot experiments. Best used for inference, finetuning should work, but is untested with this implementation."""
import os

import torch
import math
import random
from transformers.modeling_utils import SpecificPreTrainedModelType

from tqdm import tqdm
from torch import Tensor
from dataclasses import dataclass
from typing import Optional, Union, Any, Type

try:
    from train.raven_config_minimal import RavenConfig
except:
    from raven_config_minimal import RavenConfig

from transformers.cache_utils import Cache, DynamicCache

###################### Huggingface Glue code I ##################################################################
from transformers import PreTrainedModel, GenerationMixin, PretrainedConfig
from transformers.utils import ModelOutput
from transformers.generation.utils import GenerateDecoderOnlyOutput

import torch.nn.functional as F
from transformers import GenerationConfig


class RavenPreTrainedModel(PreTrainedModel):
    config_class = RavenConfig
    base_model_prefix = "model"
    supports_gradient_checkpointing = True
    _no_split_modules = ["SandwichBlock"]
    _skip_keys_device_placement = ["past_key_values"]
    _tied_weights_keys = ["lm_head.weight"]
    _supports_flash_attn_2 = True
    _supports_sdpa = True
    _supports_cache_class = True
    _supports_quantized_cache = False
    _supports_static_cache = False

    def _init_weights(self, module):
        if not torch.rand((1,)).is_meta:
            print("Random Initialization not implemented.")


@dataclass
class CausalLMOutputRecurrentLatents(ModelOutput):
    loss: Optional[torch.Tensor] = None
    log_ppl: Optional[torch.Tensor] = None
    logits: Optional[torch.Tensor] = None
    past_key_values: Optional[Cache] = None
    latent_states: Optional[torch.Tensor] = None
    hidden_states: Optional[torch.Tensor] = None
    attention_maps: Optional[dict[int, torch.Tensor]] = None
    stats: Optional[dict] = None


def svd_decompose(model, target_modules, cache_file, torch_type=None):

    def prepare(v):
        if torch_type is not None:
            v = v.to(dtype=torch_type)
        v = v.cuda()
        return  v

    if os.path.exists(cache_file):
        decompose_param_dict = torch.load(cache_file, weights_only=True)
    else:
        params_dict = model.state_dict()
        decompose_param_dict = {}
        for m in tqdm(target_modules, desc="Decomposing"):
            weight = params_dict[f"{m}.weight"]
            U, S, Vt = torch.linalg.svd(weight, full_matrices=False)
            decompose_param_dict[f"{m}.U"] =  U.contiguous()
            decompose_param_dict[f"{m}.S"] =  S.contiguous()
            decompose_param_dict[f"{m}.Vt"] =  Vt.contiguous()
        torch.save(decompose_param_dict, cache_file)

    nn_decompose_param_dict = {}

    for m in target_modules:
        nn_decompose_param_dict[f"{m}.U".replace(".", "__")] = prepare(decompose_param_dict[f"{m}.U"])
        nn_decompose_param_dict[f"{m}.S".replace(".", "__")] = prepare(decompose_param_dict[f"{m}.S"])
        nn_decompose_param_dict[f"{m}.Vt".replace(".", "__")] = prepare(decompose_param_dict[f"{m}.Vt"])

        nn_decompose_param_dict[f"{m}.U".replace(".", "__")].requires_grad = False
        nn_decompose_param_dict[f"{m}.S".replace(".", "__")].requires_grad = False
        nn_decompose_param_dict[f"{m}.Vt".replace(".", "__")].requires_grad = False

    return nn_decompose_param_dict


###################### Minimal implementation from here ############################################################


class RMSNorm(torch.nn.Module):
    """Saner dtype handling and slightly better for fusion"""

    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = torch.nn.Parameter(torch.ones(dim))

    def _norm(self, x):
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

    def forward(self, x):
        with torch.autocast(enabled=False, device_type=x.device.type if x.device.type != "meta" else "cuda"):
            return self._norm(x.float()).type_as(x) * self.weight

    def reset_parameters(self) -> None:
        torch.nn.init.ones_(self.weight)


class HuginnDynamicCache(DynamicCache):
    def __init__(self, lookup_strategy: str = "full") -> None:
        super().__init__()
        self._seen_tokens = 0
        self.key_cache: dict[int, dict[int, torch.Tensor]] = {}
        self.value_cache: dict[int, dict[int, torch.Tensor]] = {}
        # structure: cache[index_of_layer_or_recurrent_step][index_in_sequence]
        # the cache is held uncoalesced because certain recurrent steps may be missing for some sequence ids if using
        # per-token adaptive compute. In those cases, the "lookup_strategy" determines how to proceed
        # Also, It is critical that the head indices do not overlap with the recurrent iteration indices
        self.lookup_strategy = lookup_strategy

    def update(
        self,
        key_states: torch.Tensor,
        value_states: torch.Tensor,
        step_idx: int,
        lookup_strategy: Optional[str] = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        lookup_strategy = self.lookup_strategy if lookup_strategy is None else lookup_strategy
        if "compress-" in self.lookup_strategy and step_idx > 1:  # hardcode for current model!
            compression_stage = int(self.lookup_strategy.split("compress-")[1][1:])
            if "compress-s" in self.lookup_strategy:
                new_step_idx = (step_idx - 2) % compression_stage + 2
            else:
                new_step_idx = (step_idx - 2) // compression_stage + 2
            # @ print(step_idx, new_step_idx, compression_stage)
            step_idx = new_step_idx
        # Init
        if step_idx not in self.key_cache:
            self.key_cache[step_idx] = {}
            self.value_cache[step_idx] = {}
        # Update the number of seen tokens, we assume that step_idx=0 (first prelude) is always hit
        if step_idx == 0:
            self._seen_tokens += key_states.shape[-2]
        # Add entries to cache
        for idx, entry in enumerate(key_states.unbind(dim=-2)):
            if "compress-" not in self.lookup_strategy:
                assert step_idx < 0 or self._seen_tokens - key_states.shape[-2] + idx not in self.key_cache[step_idx]
            # print(f"Overwrote cache entry for step_idx {step_idx}") # likely the head
            self.key_cache[step_idx][self._seen_tokens - key_states.shape[-2] + idx] = entry
        for idx, entry in enumerate(value_states.unbind(dim=-2)):
            self.value_cache[step_idx][self._seen_tokens - value_states.shape[-2] + idx] = entry

        # Materialize past state based on lookup strategy:
        if len(self.key_cache[step_idx]) == self._seen_tokens or self.lookup_strategy == "full":
            # All entries are present, materialize cache as normal
            return (
                torch.stack(list(self.key_cache[step_idx].values()), dim=-2),
                torch.stack(list(self.value_cache[step_idx].values()), dim=-2),
            )
        else:  # some entries where not previously computed
            # if lookup_strategy.startswith("latest"):
            #     latest_keys = []
            #     latest_values = []
            #     for token_pos in range(self._seen_tokens):
            #         # Find the latest step that has this token position
            #         max_step = max((s for s in range(step_idx + 1) if token_pos in self.key_cache[s]), default=None)
            #         if max_step is None:
            #             raise ValueError(f"No cache entry found for token position {token_pos}")
            #         latest_keys.append(self.key_cache[max_step][token_pos])
            #         latest_values.append(self.value_cache[max_step][token_pos])
            #     return torch.stack(latest_keys, dim=-2), torch.stack(latest_values, dim=-2)
            if lookup_strategy.startswith("latest-m4"):
                latest_keys = []
                latest_values = []
                for token_pos in range(self._seen_tokens):
                    # For steps >= 2, use modulo 4
                    if step_idx >= 2:
                        # Find valid steps for this token position
                        valid_steps = [s for s in range(step_idx + 1) if token_pos in self.key_cache[s]]
                        max_step = max([s for s in valid_steps if s >= 2 and s % 4 == step_idx % 4])
                    else:
                        max_step = step_idx if token_pos in self.key_cache[step_idx] else 0
                    if max_step is None:
                        raise ValueError(f"No cache entry found for token position {token_pos}")
                    latest_keys.append(self.key_cache[max_step][token_pos])
                    latest_values.append(self.value_cache[max_step][token_pos])
                return torch.stack(latest_keys, dim=-2), torch.stack(latest_values, dim=-2)
            elif lookup_strategy.startswith("skip"):
                existing_keys = []
                existing_values = []
                for token_pos in range(self._seen_tokens):
                    if token_pos in self.key_cache[step_idx]:
                        existing_keys.append(self.key_cache[step_idx][token_pos])
                        existing_values.append(self.value_cache[step_idx][token_pos])
                return torch.stack(existing_keys, dim=-2), torch.stack(existing_values, dim=-2)
            elif lookup_strategy.startswith("randomized"):  # sanity check
                rand_keys = []
                rand_values = []
                for token_pos in range(self._seen_tokens):
                    if step_idx < 2:  # For prelude steps
                        max_step = step_idx if token_pos in self.key_cache[step_idx] else 0
                    else:  # Get all steps from same block position
                        curr_modulo = (step_idx - 2) % 4 + 2
                        valid_steps = [
                            s
                            for s in range(2, step_idx + 1)
                            if (s - 2) % 4 + 2 == curr_modulo and token_pos in self.key_cache[s]
                        ]
                        max_step = valid_steps[torch.randint(len(valid_steps), (1,))]
                    rand_keys.append(self.key_cache[max_step][token_pos])
                    rand_values.append(self.value_cache[max_step][token_pos])
                return torch.stack(rand_keys, dim=-2), torch.stack(rand_values, dim=-2)
            else:
                raise ValueError(f"Unknown lookup strategy: {lookup_strategy}")

    def reset(self) -> None:
        """Reset the cache state."""
        self._seen_tokens = 0
        self.key_cache.clear()
        self.value_cache.clear()

    def get_seq_length(self, step_idx: int = 0) -> int:
        return self._seen_tokens

    def get_memory_usage(self) -> float:
        total_bytes = 0
        # For each recurrent step/layer index
        for step_idx in self.key_cache:
            # Get the sequence cache for this step
            key_seq_cache = self.key_cache[step_idx]
            for seq_idx in key_seq_cache:
                key_tensor = key_seq_cache[seq_idx]
                # Add memory for of key tensors, assuming value is the same
                total_bytes += key_tensor.nelement() * key_tensor.element_size()
        return total_bytes * 2 / (1024 * 1024)


class CausalSelfAttention(torch.nn.Module):
    def __init__(self, config: RavenConfig) -> None:
        super().__init__()
        self.config = config
        self.n_head = config.num_attention_heads
        self.n_kv_heads = config.num_key_value_heads
        self.head_dim = config.n_embd // self.n_head

        shape = (self.n_head + 2 * self.n_kv_heads) * self.head_dim
        self.chunks = [config.n_embd, self.n_kv_heads * self.head_dim, self.n_kv_heads * self.head_dim]
        self.Wqkv = torch.nn.Linear(config.n_embd, shape, bias=False)
        if config.qk_bias:
            self.qk_bias = torch.nn.Parameter(torch.zeros(2, 1, self.n_head, self.head_dim))
        self.proj = torch.nn.Linear(config.n_embd, config.n_embd, bias=False)

    def forward(
        self,
        x: Tensor,
        freqs_cis: Tensor,
        step_idx: int,
        mask: Optional[Tensor] = None,
        past_key_values: Optional[Cache] = None,
        return_attn: bool = False,
    ) -> tuple[Tensor, Optional[Tensor]]:
        B, S, E = x.shape  # batch size, sequence length, embedding dimensionality (n_embd)
        q, k, v = self.Wqkv(x).split(self.chunks, dim=2)
        q = q.view(B, S, self.n_head, self.head_dim)
        k = k.view(B, S, self.n_kv_heads, self.head_dim)
        v = v.view(B, S, self.n_kv_heads, self.head_dim)
        # bias?
        if self.config.qk_bias:
            q_bias, k_bias = self.qk_bias.split(1, dim=0)
            q, k = (q + q_bias).to(q.dtype), (k + k_bias).to(q.dtype)
        # apply rotary
        q, k = apply_rotary_emb_complex_like(q, k, freqs_cis=freqs_cis)

        q = q.transpose(1, 2)  # (B, nh, S, hs)
        k = k.transpose(1, 2)
        v = v.transpose(1, 2)

        if past_key_values is not None:
            k, v = past_key_values.update(k, v, step_idx)

        if return_attn:
            y, attention_map = self.compute_eager_sdpa(q, k, v, attn_mask=mask)
        else:
            if mask is not None:
                mask = mask[:, None, :]
                mask_ = mask.unsqueeze(1).expand(mask.shape[0], q.shape[1], mask.shape[-1], mask.shape[-1])
                mask = mask_.clone().float()
                mask = mask.masked_fill_(mask_ == 0, -float("inf"))
            y = torch.nn.functional.scaled_dot_product_attention(
                q, k, v, attn_mask=mask, dropout_p=0.0, is_causal=q.shape[2] > 1
            )
        y = y.transpose(1, 2).reshape(B, S, E).contiguous()  # reshape is a view if possible (it mostly is)
        return self.proj(y), attention_map if return_attn else None

    def compute_eager_sdpa(self, q, k, v, attn_mask):
        scale = 1.0 / math.sqrt(self.head_dim)
        scores = torch.matmul(q, k.transpose(-2, -1)) * scale

        if attn_mask is not None:
            attn_mask = attn_mask[:, None, None, :]  # [batch_size, 1, 1, seq_len]
            attn_mask = attn_mask.expand(-1, q.size(1), q.size(2), -1)  # [batch_size, num_heads, seq_len, seq_len]
            attn_mask = torch.where(attn_mask == 1, 0.0, float('-inf'))
            scores = scores + attn_mask
        if q.shape[2] > 1:
            causal_mask = torch.triu(torch.ones(q.shape[2], q.shape[2]), diagonal=1).bool()
            scores.masked_fill_(causal_mask.to(scores.device), float("-inf"))

        attention_weights = torch.nn.functional.softmax(scores, dim=-1)
        y = torch.matmul(attention_weights, v)
        return y, attention_weights.max(dim=1)[0]


class GatedMLP(torch.nn.Module):
    def __init__(self, config: RavenConfig, in_features: int = 0) -> None:
        super().__init__()
        in_features = config.n_embd if in_features == 0 else in_features
        self.fc = torch.nn.Linear(in_features, config.intermediate_size * 2, bias=False)

        self.proj = torch.nn.Linear(config.intermediate_size, config.n_embd, bias=False)
        self.nonlin = torch.nn.SiLU()

    def forward(self, x: Tensor) -> Tensor:
        # modified to single FC layer to improve parallelism
        x_fc_1, x_fc_2 = self.fc(x).chunk(2, dim=-1)
        x = self.nonlin(x_fc_1) * x_fc_2
        return self.proj(x)


class LoRAHook:

    def __init__(self, weight_type, scaling, decompose_param_dict):
        self.weight_type = weight_type  # is one of Wqkv, pojo
        self.scaling = scaling
        self.decompose_param_dict = decompose_param_dict

        self.branch_inx = None
        self.block_inx = None
    
    def __call__(self, moudle, input, output):
        if self.block_inx is not None:
            assert self.weight_type is not None
            assert self.block_inx is not None
            assert self.branch_inx is not None
            prefix = f"transformer.core_block.{self.block_inx}.attn.{self.weight_type}.{self.branch_inx}"
            A = self.decompose_param_dict[f"{prefix}.A".replace(".", "__")]
            B = self.decompose_param_dict[f"{prefix}.B".replace(".", "__")]
            delta = torch.matmul(torch.matmul(input[0], B), A)
            return output + delta * self.scaling
        else:
            return output   

def merge_svd_matrix(decompose_param_dict, vectors_param_dict, branch_inx, block_inx, weight_type):

    weight_key = f"transformer.core_block.{block_inx}.attn.{weight_type}"
    weight_singular_key = f"transformer.core_block.{block_inx}.attn.{weight_type}.{branch_inx}.singular_scale"

    U = decompose_param_dict[f"{weight_key}.U".replace(".", "__")]
    S = decompose_param_dict[f"{weight_key}.S".replace(".", "__")]
    Vt = decompose_param_dict[f"{weight_key}.Vt".replace(".", "__")]
    Z = vectors_param_dict[weight_singular_key.replace(".", "__")]

    Z = torch.sigmoid(Z)
    W_ = torch.matmul(U, torch.matmul(torch.diag(S * Z), Vt))
    W_ = W_ * (S.sum() / Z.sum())
    return  W_

class SVDHook:

    def __init__(self, weight_type, model):
        self.weight_type = weight_type
        self.model = model

        self.block_inx = None
        self.branch_inx = None

    @property
    def decompose_param_dict(self):
        return self.model.svd_decompose_param_dict

    @property
    def vectors_param_dict(self):
        return self.model.vectors_param_dict

    def __call__(self, moudle, input, output):
        assert self.block_inx is not None
        assert self.branch_inx is not None
        if self.model.training or self.model.svd_merged_weights is None:
            W_ = merge_svd_matrix(self.decompose_param_dict, self.vectors_param_dict,
                                  self.branch_inx, self.block_inx, self.weight_type)
        else:
            weight_key = f"transformer.core_block.{self.block_inx}.attn.{self.weight_type}.{self.branch_inx}"
            W_ = self.model.svd_merged_weights[weight_key]

        output_ = input[0] @ W_.T
        return output_


class SandwichBlock(torch.nn.Module):
    expanded = False

    def __init__(self, config: RavenConfig, layer_id: int) -> None:
        super().__init__()
        self.norm_1 = RMSNorm(config.n_embd, eps=config.norm_eps)
        self.attn = CausalSelfAttention(config)
        self.norm_2 = RMSNorm(config.n_embd, eps=config.norm_eps)
        self.mlp = GatedMLP(config)
        self.norm_3 = RMSNorm(config.n_embd, eps=config.norm_eps)
        self.norm_4 = RMSNorm(config.n_embd, eps=config.norm_eps)
        self.layer_id = layer_id

    def forward(
        self,
        x: Tensor,
        freqs_cis: Tensor,
        step_idx: int,
        mask: Optional[Tensor] = None,
        past_key_values: Optional[Cache] = None,
        return_attn: bool = False,
    ) -> tuple[Tensor, Optional[Tensor]]:
        attn_out, attn_map = self.attn(self.norm_1(x), freqs_cis, step_idx, mask, past_key_values, return_attn)
        x = self.norm_2(attn_out + x)
        x = self.norm_4(self.mlp(self.norm_3(x)) + x)
        return x, attn_map


class RavenRouter(torch.nn.Module):

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.top_k = config.num_branches_per_tok
        self.num_branches = config.num_branches

        self.scoring_func = config.scoring_func
        self.alpha = config.aux_loss_alpha
        self.seq_aux = config.seq_aux
        self.topk_method = config.topk_method
        self.n_group = config.n_group
        self.topk_group = config.topk_group
        self.routed_scaling_factor = config.routed_scaling_factor

        # topk selection algorithm
        self.norm_topk_prob = config.norm_topk_prob
        self.gating_dim = config.n_embd
        self.weight = torch.nn.Parameter(
            torch.empty((self.num_branches, self.gating_dim)),
            )
        if self.topk_method == "noaux_tc":
            self.e_score_correction_bias = torch.nn.Parameter(
                torch.zeros((self.num_branches)))

        self.reset_parameters()

    def reset_parameters(self) -> None:
        import torch.nn.init  as init
        init.kaiming_uniform_(self.weight, a=math.sqrt(5))

    def forward(self, hidden_states, mask=None):
        bsz, seq_len, h = hidden_states.shape   # [bsz, seq_len, h]
        ### compute gating score
        hidden_states = hidden_states.view(-1, h) # [bsz * seq_len, h]
        logits = F.linear(hidden_states, self.weight, None) # [bsz * seq_len, num_branches]
        logits = logits.view(bsz, seq_len, -1)
        if mask is not None:
            float_mask = mask.unsqueeze(-1).to(logits.dtype) # [bsz, seq_len, 1]
            logits = logits * float_mask
            valid_counts = mask.sum(dim=1, keepdim=True).to(logits.dtype) # [bsz, 1]
            valid_counts = valid_counts + 1e-8 
            logits = logits.sum(dim=1) / valid_counts # [bsz, num_branches]
        else:
            logits = logits.mean(dim=1)
        if self.scoring_func == 'softmax':
            scores = logits.softmax(dim=-1) # [bsz, num_branches]
        elif self.scoring_func == 'sigmoid':
            scores = logits.sigmoid()  # [bsz, num_branches]
        else:
            raise NotImplementedError(f'insupportable scoring function for MoE gating: {self.scoring_func}')

        ### select top-k branches
        if self.topk_method == "noaux_tc":
            scores_for_choice = scores + self.e_score_correction_bias # [bsz, num_branches]
            _, topk_idx = torch.topk(scores_for_choice, k=self.top_k, dim=-1, sorted=False) # [bsz, topk]
            topk_weight = scores.gather(1, topk_idx) # [bsz, topk]
        else:
            _, topk_idx = torch.topk(scores, k=self.top_k, dim=-1, sorted=False)  # [bsz, topk], [bsz, topk]
            topk_weight = scores.gather(1, topk_idx) # [bsz, topk]

        ### norm gate to sum 1
        if self.top_k > 1 and self.norm_topk_prob:
            denominator = topk_weight.sum(dim=-1, keepdim=True) + 1e-20
            topk_weight = topk_weight / denominator
        else:
            topk_weight = topk_weight * self.routed_scaling_factor

        ## branch-level computation auxiliary loss
        if self.training and self.alpha > 0.0:
            scores_for_aux = scores # [bsz, num_branches]
            aux_topk = self.top_k   # top_k
            # always compute aux loss based on the naive greedy topk method
            topk_idx_for_aux_loss = topk_idx.view(bsz, -1)  # [bsz, topk]
            if self.seq_aux:
                scores_for_seq_aux = scores_for_aux.view(bsz, -1) # [bsz, num_branches]
                ce = torch.zeros(bsz, self.num_branches, device=hidden_states.device) # [bsz, num_branches]
                ce.scatter_add_(1, topk_idx_for_aux_loss, torch.ones(bsz, aux_topk, device=hidden_states.device)).div_(bsz / self.num_branches)
                aux_loss = (ce * scores_for_seq_aux).sum(dim = 1).mean() * self.alpha # [bsz, num_branches] * [bsz, num_branches]
            else:
                mask_ce = F.one_hot(topk_idx_for_aux_loss.view(-1), num_classes=self.num_branches)  # [bsz * topk, num_branches]
                ce = mask_ce.float().mean(0)    # [num_branches]
                Pi = scores_for_aux.mean(0) # [num_branches]
                fi = ce * self.num_branches
                aux_loss = (Pi * fi).sum() * self.alpha
        else:
            aux_loss = None

        return topk_idx, topk_weight, aux_loss


class AddAuxiliaryLoss(torch.autograd.Function):
    """
    The trick function of adding auxiliary (aux) loss,
    which includes the gradient of the aux loss during backpropagation.
    """
    @staticmethod
    def forward(ctx, x, loss):
        assert loss.numel() == 1
        ctx.dtype = loss.dtype
        ctx.required_aux_loss = loss.requires_grad
        return x

    @staticmethod
    def backward(ctx, grad_output):
        grad_loss = None
        if ctx.required_aux_loss:
            grad_loss = torch.ones(1, dtype=ctx.dtype, device=grad_output.device)
        return grad_output, grad_loss


class RavenForCausalLM(RavenPreTrainedModel, GenerationMixin):

    W_TYPE_ATTN_Wqkv = "Wqkv"
    W_TYPE_ATTN_proj = "proj"

    def __init__(
        self,
        config: RavenConfig,
    ) -> None:
        super().__init__(config)
        self.config = config

        # Transformer layers
        prelude = torch.nn.ModuleList(SandwichBlock(config, layer_id=i) for i in range(config.n_layers_in_prelude))
        adapter = torch.nn.Linear(config.n_embd * 2, config.n_embd, bias=config.bias)
        core_block = torch.nn.ModuleList(
            SandwichBlock(config, layer_id=i + config.n_layers_in_prelude)
            for i in range(config.n_layers_in_recurrent_block)
        )
        o = config.n_layers_in_prelude + config.n_layers_in_recurrent_block * config.mean_recurrence
        coda = torch.nn.ModuleList(SandwichBlock(config, layer_id=i + o) for i in range(config.n_layers_in_coda))

        self.transformer = torch.nn.ModuleDict(
            dict(
                wte=torch.nn.Embedding(config.padded_vocab_size, config.n_embd),
                prelude=prelude,
                adapter=adapter,
                core_block=core_block,
                coda=coda,
                ln_f=RMSNorm(config.n_embd, eps=config.norm_eps),  # used twice :>
            )
        )
        self.emb_scale = config.init_values["embed_scale"]

        # Decomposition
        fine_tuning_algorithm: str = config.fine_tuning_algorithm

        lora_decompose_param_dict = None
        vectors_param_dict = None
        if fine_tuning_algorithm == "svd":
            vectors_param_dict = self.init_branch_vectors()

        elif fine_tuning_algorithm == "lora":
            lora_decompose_param_dict = self.init_lora_decompose()

        self.lora_decompose_param_dict = lora_decompose_param_dict
        self.vectors_param_dict: torch.nn.ParameterDict = vectors_param_dict

        self.svd_decompose_param_dict: dict[str, torch.Tensor] = None
        self.svd_merged_weights: dict[str, torch.Tensor] = None

        ########################## Add adaptive router mechanism
        if self.config.router_type == "gate":
            self.router = torch.nn.ModuleList([RavenRouter(config) for _ in range(self.config.num_choices)])
        else:
            self.router = None
        # self.router = RavenRouter(config)
        self._moe_router_counts = []
        self.topk_idxs = []
        ##########################

        # Head
        self.lm_head = torch.nn.Linear(config.n_embd, config.padded_vocab_size, bias=False)
        if self.config.tie_embeddings:
            self.tie_weights()

        # rope
        self.register_buffer("freqs_cis", self._precompute_freqs_cis(), persistent=True)

    def init_lora_decompose(self):
        lora_r = self.config.lora_r
        num_branches = self.config.num_branches
        target_modules = self.config.target_modules

        def low_rank_d(mud):
            if self.W_TYPE_ATTN_Wqkv in mud:
                d, k = (self.config.n_embd, self.config.n_embd * 3)
            else:
                d, k = (self.config.n_embd, self.config.n_embd)
            B = torch.zeros(size=(d, lora_r), requires_grad=True)
            A = torch.empty((lora_r, k), requires_grad=True)   
            return A, B

        decompose_param_dict = torch.nn.ParameterDict()
        for i in range(num_branches):
            for mdu in target_modules:
                A, B = low_rank_d(mdu)  # Linear actually is: x @ W^t
                decompose_param_dict[f"{mdu}.{i}.A".replace(".", "__")] = torch.nn.Parameter(A)
                decompose_param_dict[f"{mdu}.{i}.B".replace(".", "__")] = torch.nn.Parameter(B)
        return decompose_param_dict

    def init_branch_vectors(self):
        vectors_param_dict = {}
        num_branches = self.config.num_branches
        for i in range(num_branches):
            for j in range(4):
                Wqkv_key = f"transformer.core_block.{j}.attn.Wqkv"
                proj_key = f"transformer.core_block.{j}.attn.proj"
                Wqkv_scale = torch.normal(mean=0.1, std=1e-3, size=(self.config.n_embd,), requires_grad=True)
                vectors_param_dict[f"{Wqkv_key}.{i}.singular_scale".replace(".", "__")] = Wqkv_scale
                proj_scale = torch.normal(mean=0.1, std=1e-3, size=(self.config.n_embd,), requires_grad=True)
                vectors_param_dict[f"{proj_key}.{i}.singular_scale".replace(".", "__")] = proj_scale
        nn_vectors_param_dict = torch.nn.ParameterDict(vectors_param_dict)
        return nn_vectors_param_dict

    def apply_lora_hook(self):
        scaling = self.config.lora_alpha / self.config.lora_r
        # add hook to attention module
        for block in self.transformer.core_block:
            Wqkv_hook = LoRAHook(self.W_TYPE_ATTN_Wqkv, scaling, self.lora_decompose_param_dict)
            block.attn.Wqkv.register_forward_hook(Wqkv_hook)

            proj_hook = LoRAHook(self.W_TYPE_ATTN_proj, scaling, self.lora_decompose_param_dict)
            block.attn.proj.register_forward_hook(proj_hook)

    def apply_svd_hook(self):
        for block in self.transformer.core_block:
            Wqkv_hook = SVDHook(self.W_TYPE_ATTN_Wqkv, self)
            block.attn.Wqkv.register_forward_hook(Wqkv_hook)

            proj_hook = SVDHook(self.W_TYPE_ATTN_proj, self)
            block.attn.proj.register_forward_hook(proj_hook)

    def reset_parameters(self, init_lora=True) -> None:
        if self.config.fine_tuning_algorithm == 'lora':
            if init_lora:
                for name, param in self.lora_decompose_param_dict.named_parameters():
                    if name.endswith("__A"):
                        # A = torch.normal(mean=0, std=1 / lora_r, size=(lora_r, k), requires_grad=True)
                        torch.nn.init.kaiming_uniform_(param, a=math.sqrt(5))

        if self.config.router_type == "gate":
            try:
                self.router.reset_parameters()
            except:
                for router in self.router:
                    try:
                        router.reset_parameters()
                    except:
                        pass

    def merge_svd_weights(self):
        block_nums = 4
        merged_dict = {}
        for branch_inx in range(self.config.num_branches):
            for block_inx in range(block_nums):
                for weight_type in [self.W_TYPE_ATTN_Wqkv, self.W_TYPE_ATTN_proj]:
                    W_ = merge_svd_matrix(self.svd_decompose_param_dict, self.vectors_param_dict,
                                          branch_inx, block_inx, weight_type)
                    weight_key = f"transformer.core_block.{block_inx}.attn.{weight_type}.{branch_inx}"
                    merged_dict[weight_key] = W_
        self.svd_merged_weights = merged_dict

    def get_input_embeddings(self):
        return self.transformer.wte

    def get_output_embeddings(self):
        return self.lm_head

    def _precompute_freqs_cis(self):
        # can actually be a buffer now, and remains in fp32! (at least in the settings I tested)
        freqs_cis = precompute_freqs_cis(
            self.config.n_embd // self.config.num_attention_heads, self.config.block_size, self.config.rope_base, 1
        )
        return freqs_cis

    def sft_loss_function(self, logits, labels, vocab_size: int, num_items_in_batch: int = None, ignore_index: int = -100):
        # 1. obtain y proba
        logits = logits[..., :-1, :].contiguous()  # remove last time step logits
        # 1.1. utilize softmax to obtain probability
        y_proba = torch.nn.functional.softmax(logits, dim=-1)  # y_proba: (batch_size, seq_length - 1, vocab_size)
        y_pred = torch.argmax(y_proba, dim=-1)  # y_pred: (batch_size, seq_length - 1)

        # 2. obtain ground truth
        # inputs: (batch_size, seq_length)
        labels = labels[..., 1:].contiguous()  # labels: (batch_size, seq_length - 1)

        mask = (labels != -100)
        valid_labels = labels[mask]
        valid_preds = y_pred[mask]

        if len(valid_labels) > 0:
            correct = (valid_preds == valid_labels).sum().item()
            acc = correct / len(valid_labels)
        else:
            acc = 0.0 
        print(f"Tokens Accuracy: {acc}")

        # 3. Masked cross entropy
        flat_labels = labels.reshape(-1)
        flat_logits = logits.reshape((-1, vocab_size))
        masked_loss = torch.nn.functional.cross_entropy(flat_logits, flat_labels, reduction='mean', ignore_index=-100)
        return masked_loss

    @classmethod
    def from_pretrained(
        cls: Type[SpecificPreTrainedModelType],
        pretrained_model_name_or_path: Optional[Union[str, os.PathLike]],
        *model_args,
        config: Optional[Union[PretrainedConfig, str, os.PathLike]] = None,
        cache_dir: Optional[Union[str, os.PathLike]] = None,
        ignore_mismatched_sizes: bool = False,
        force_download: bool = False,
        local_files_only: bool = False,
        token: Optional[Union[str, bool]] = None,
        revision: str = "main",
        use_safetensors: Optional[bool] = None,
        weights_only: bool = True,
        **kwargs,
    ) -> SpecificPreTrainedModelType:
        model = super().from_pretrained(pretrained_model_name_or_path,
                                *model_args,
                                config=config, cache_dir=cache_dir, ignore_mismatched_sizes=ignore_mismatched_sizes,
                                force_download=force_download, local_files_only=local_files_only, token=token,
                                revision=revision, use_safetensors=use_safetensors,
                                weights_only=weights_only, **kwargs)

        torch_type = kwargs.get('torch_dtype')
        if model.config.fine_tuning_algorithm == 'svd':

            model.svd_decompose_param_dict = svd_decompose(model, model.config.target_modules,
                                                           model.config.svd_cache_file, torch_type=torch_type)
            if torch_type is not None:
                for k, v in model.vectors_param_dict.items():
                    model.vectors_param_dict[k] = v.to(dtype=torch_type)
        elif model.config.fine_tuning_algorithm == 'lora':
            if torch_type is not None:
                for k, v in model.lora_decompose_param_dict.items():
                    model.lora_decompose_param_dict[k] = v.to(dtype=torch_type)

        return model

    def forward(
        self,
        input_ids: torch.Tensor,
        input_embeds: Optional[torch.Tensor] = None,
        input_states: Optional[torch.Tensor] = None,
        attention_mask: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.Tensor] = None,
        labels: Optional[torch.Tensor] = None,
        num_steps: Optional[torch.Tensor] = None,
        num_choices: Optional[int] = None,
        past_key_values: Optional[Cache] = None,
        output_details: dict = {
            "return_logits": True,
            "return_latents": True,
            "return_attention": False,
            "return_head": False,
            "return_stats": False,
        },
        use_cache: bool = False,
        cache_position: Optional[torch.Tensor] = None,
        **kwargs,
    ) -> CausalLMOutputRecurrentLatents:
        # Support multiple position formats:
        if position_ids is None and cache_position is None:
            freqs_cis = self.freqs_cis[:, : input_ids.shape[1]]
        elif position_ids is not None:
            freqs_cis = self.freqs_cis.index_select(1, position_ids.squeeze())
        elif cache_position is not None:
            freqs_cis = self.freqs_cis[:, cache_position]
        if not self.training and num_steps is None:
            num_steps = (self.config.num_steps[0], self.config.num_steps[1])
        if input_embeds is None:
            input_embeds = self.transformer.wte(input_ids)

        if self.emb_scale != 1:
            input_embeds = input_embeds * self.emb_scale  # type: ignore

        if use_cache and past_key_values is None:
            past_key_values = HuginnDynamicCache()
        attn_maps = {}
        return_attn = output_details["return_attention"]

        # Non-recurrent prelude
        for block_idx, block in enumerate(self.transformer.prelude):
            input_embeds, attn_map = block(
                input_embeds, freqs_cis, block_idx, attention_mask, past_key_values, return_attn=return_attn
            )
            attn_maps[block_idx] = attn_map

        x, num_steps_no_grad, num_steps_with_grad, xk, block_idx, attn_maps = self.iterate_forward(
            input_embeds=input_embeds,  # type: ignore
            input_states=input_states,
            freqs_cis=freqs_cis,
            block_idx=block_idx,
            mask=attention_mask,
            past_key_values=past_key_values,
            num_steps=num_steps,
            num_choices=num_choices,
            attn_maps=attn_maps,
            return_attn=return_attn,
        )

        latent_states = x.clone().detach()

        # Coda layers
        for block_idx, block in enumerate(self.transformer.coda, start=1):
            x, attn_map = block(x, freqs_cis, -block_idx, attention_mask, past_key_values, return_attn=return_attn)
            attn_maps[-block_idx] = attn_map
        x = self.transformer.ln_f(x)

        # Prediction head, assuming labels really are labels and not equal to input_ids
        if labels is not None:
            logits = self.lm_head(x).float()
            loss = self.sft_loss_function(logits, labels, vocab_size=logits.shape[-1], ignore_index=-100)
            #loss = torch.nn.functional.cross_entropy(logits.view(-1, logits.shape[-1]), labels.view(-1))
            # log_ppl = loss.clone().detach().exp()
            log_ppl = torch.as_tensor(0.0)
        else:
            logits = self.lm_head(x).float()
            loss, log_ppl = torch.as_tensor(0.0), torch.as_tensor(0.0)

        return CausalLMOutputRecurrentLatents(
            loss=loss,
            log_ppl=log_ppl,
            logits=logits if output_details["return_logits"] else None,
            past_key_values=past_key_values,
            hidden_states=x if output_details["return_head"] else None,
            latent_states=latent_states if output_details["return_latents"] else None,
            attention_maps=attn_maps if output_details["return_attention"] else None,  # type: ignore
            stats=self.get_stats(logits, x, latent_states, xk, input_embeds, num_steps_no_grad, num_steps_with_grad)
            if output_details["return_stats"]
            else None,
        )

    @torch._dynamo.disable(recursive=False)  # type: ignore
    def iterate_forward(
        self,
        input_embeds,
        input_states,
        freqs_cis,
        block_idx,
        mask,
        past_key_values: Optional[Cache] = None,
        num_steps: Optional[torch.Tensor] = None,
        num_choices: int = None,
        attn_maps: dict = {},
        return_attn: bool = False,
    ):
        x = self.initialize_state(input_embeds) if input_states is None else input_states.clone()

        if num_steps is None:
            num_steps_no_grad, num_steps_with_grad = self.randomized_iteration_sampler()  # type: ignore
        elif hasattr(num_steps, "__len__") and len(num_steps) > 1:
            num_steps_no_grad, num_steps_with_grad = num_steps
        else:
            num_steps_no_grad, num_steps_with_grad = num_steps, torch.tensor(0) if not x.is_meta else 0

        num_choices = getattr(self.config, 'num_choices') if num_choices is None else num_choices

        if self.training and num_choices > 1:
            num_steps_no_grad = max(1, math.ceil(num_steps_no_grad / num_choices))
            num_steps_with_grad = max(1, math.ceil(num_steps_with_grad / num_choices))

        choice_counts = {}
        for bs in range(x.shape[0]):
            choice_counts[f"sample_{bs}"] = []
        aux_losses = 0
        aux_loss = None
        out_x = []
        for idx_router in range(num_choices):
            if self.config.router_type == "normal":
                topk_weight, aux_loss = 0, None
                topk_idx = random.randint(0, self.config.num_branches - 1)
            elif self.config.router_type == "random":
                if self.config.router_choice_idx is None:
                    topk_idx = random.sample(range(self.config.num_branches), x.shape[0])
                    topk_idx = torch.tensor([topk_idx], dtype=torch.int).to(x.device).reshape(x.shape[0], 1)
                    topk_weight = torch.tensor([[1]*x.shape[0]], dtype=input_embeds.dtype).to(x.device).reshape(x.shape[0], 1)
                    aux_loss = None
                else:
                    topk_idx = torch.tensor([[self.config.router_choice_idx]], dtype=torch.int).to(x.device)
                    topk_weight = torch.tensor([[1]], dtype=input_embeds.dtype).to(x.device)
                    aux_loss = None
            elif self.config.router_type == "gate":
                if self.config.router_choice_idx is None:
                    input_router = self.transformer.adapter(torch.cat([x, input_embeds.to(x.device)], dim=-1))
                    topk_idx, topk_weight, aux_loss = self.router[idx_router](input_router, mask=mask) 
                    # if self.training or num_choices > 1:
                    #     input_router = self.transformer.adapter(torch.cat([x, input_embeds.to(x.device)], dim=-1))
                    #     topk_idx, topk_weight, aux_loss = self.router[idx_router](input_router, mask=mask)                         
                    # else:
                    #     topk_idx_count = []
                    #     for _ in range(10):
                    #         x = self.initialize_state(input_embeds) if input_states is None else input_states.clone()
                    #         input_router = self.transformer.adapter(torch.cat([x, input_embeds.to(x.device)], dim=-1))
                    #         topk_idx, topk_weight, aux_loss = self.router[idx_router](input_router, mask=mask) 
                    #         topk_idx_count.append(topk_idx.item())
                    #     topk_idx_count = Counter(topk_idx_count)
                    #     topk_idx = max(topk_idx_count, key=topk_idx_count.get)
                    #     topk_idx = torch.tensor([[topk_idx]], dtype=torch.int).to(x.device)
                    #     topk_weight = torch.tensor([[1]], dtype=input_embeds.dtype).to(x.device)
                    #     aux_loss = None

                    #     while True:
                    #         x = self.initialize_state(input_embeds) if input_states is None else input_states.clone()
                    #         input_router_ = self.transformer.adapter(torch.cat([x, input_embeds.to(x.device)], dim=-1))
                    #         topk_idx_, _, _ = self.router[idx_router](input_router_, mask=mask) 
                    #         if topk_idx_.item() == topk_idx.item():
                    #             break
                else:
                    if self.config.router_choice_idx == 'random':
                        topk_idx = random.sample(range(self.config.num_branches), x.shape[0])
                        topk_idx = torch.tensor([topk_idx], dtype=torch.int).to(x.device).reshape(x.shape[0], 1)
                        topk_weight = torch.tensor([[1]*x.shape[0]], dtype=input_embeds.dtype).to(x.device).reshape(x.shape[0], 1)
                        aux_loss = None
                    else:
                        topk_idx = torch.tensor([[self.config.router_choice_idx]], dtype=torch.int).to(x.device)
                        topk_weight = torch.tensor([[1]], dtype=input_embeds.dtype).to(x.device)
                        aux_loss = None

                aux_losses += aux_loss if aux_loss is not None else 0
                self.topk_idxs.append(topk_idx)
            
            if self.config.router_type in ["random", "gate"]:
                for bs in range(x.shape[0]):
                    try:
                        try:
                            choice_counts[f"sample_{bs}"].append(topk_idx[bs].data.tolist())
                        except:
                            choice_counts[f"sample_{bs}"].append(topk_idx[bs].item())
                    except:
                        choice_counts[f"sample_{bs}"].append(topk_idx[bs])

            with torch.no_grad():
                # ultra annoying in ddp due to
                # https://discuss.pytorch.org/t/does-distributeddataparallel-work-with-torch-no-grad-and-find-unused-parameters-false/122594
                # for now running with find_unused_params=True enabled even though the graph structure is (technically) clear
                # and all parameters are always used
                for step in range(num_steps_no_grad):
                    if self.config.router_type == "normal":
                        x, block_idx, attn_maps = self.core_block_forward(
                            x=x,
                            input_embeds=input_embeds,
                            branch_idx=topk_idx,
                            freqs_cis=freqs_cis,
                            mask=mask,
                            past_key_values=past_key_values,
                            block_idx=block_idx,
                            attn_maps=attn_maps,
                            return_attn=return_attn)
                    else:
                        x, block_idx, attn_maps = self.route_core_block_forward(
                            x=x,
                            topk_idx=topk_idx,
                            topk_weight=topk_weight,
                            input_embeds=input_embeds,
                            freqs_cis=freqs_cis, mask=mask, past_key_values=past_key_values,
                            block_idx=block_idx, attn_maps=attn_maps, return_attn=return_attn)

            for step in range(num_steps_with_grad):
                if self.config.router_type == "normal":
                    x, block_idx, attn_maps = self.core_block_forward(
                        x=x,
                        input_embeds=input_embeds,
                        branch_idx=topk_idx,
                        freqs_cis=freqs_cis,
                        mask=mask,
                        past_key_values=past_key_values,
                        block_idx=block_idx,
                        attn_maps=attn_maps,
                        return_attn=return_attn)
                else:
                    x, block_idx, attn_maps = self.route_core_block_forward(
                        x,
                        topk_idx=topk_idx,
                        topk_weight=topk_weight,
                        input_embeds=input_embeds,
                        freqs_cis=freqs_cis, mask=mask, past_key_values=past_key_values,
                        block_idx=block_idx, attn_maps=attn_maps, return_attn=return_attn)

            if self.config.router_type == "gate" and num_choices > 1:
                if idx_router != num_choices - 1:
                    out_x.append(x)
                else:
                    out_x.append(x)

            if aux_loss is not None:
                x = AddAuxiliaryLoss.apply(x, aux_loss)

        if self.config.router_type == "gate" and len(out_x) > 1:
            x = torch.mean(torch.stack(out_x), dim=0)

        self._moe_router_counts.clear()
        self._moe_router_counts.append(choice_counts)
        self._moe_router_counts.append(aux_losses/num_choices)

        if not self.training and choice_counts != {}:
            self.trajectory_choice_idx.append(choice_counts)

        return self.transformer.ln_f(x), num_steps_no_grad, num_steps_with_grad, x.detach(), block_idx, attn_maps

    def core_block_forward(self, *args, **kwargs):
        if self.config.fine_tuning_algorithm == 'svd':
            return self.core_block_forward_svd(*args, **kwargs)
        elif self.config.fine_tuning_algorithm == 'lora':
            return self.core_block_forward_lora(*args, **kwargs)
        else:
            return self.core_block_forward_raw(*args, **kwargs)

    def core_block_forward_raw(
        self,
        x,
        input_embeds,
        branch_idx,
        freqs_cis,
        mask,
        past_key_values,
        block_idx: Union[torch.Tensor, int],
        attn_maps: dict = {},
        return_attn: bool = False,
    ):
        xk = x
        xk = self.transformer.adapter(torch.cat([xk, input_embeds.to(x.device)], dim=-1))
        for idx, block in enumerate(self.transformer.core_block, start=1):
            xk, attn_map = block(xk, freqs_cis, block_idx + idx, mask, past_key_values, return_attn=return_attn)
            attn_maps[block_idx + idx] = attn_map
        return xk, block_idx + idx, attn_maps

    def core_block_forward_svd(
        self,
        x,
        input_embeds,
        branch_idx,
        freqs_cis,
        mask,
        past_key_values,
        block_idx: Union[torch.Tensor, int],
        attn_maps: dict = {},
        return_attn: bool = False,
    ):
        xk = x
        xk = self.transformer.adapter(torch.cat([xk, input_embeds.to(xk.device)], dim=-1))
        for block_id, block in enumerate(self.transformer.core_block):
            Wqkv_hook = list(block.attn.Wqkv._forward_hooks.values())[0]
            proj_hook = list(block.attn.proj._forward_hooks.values())[0]

            assert isinstance(Wqkv_hook, SVDHook)
            assert isinstance(proj_hook, SVDHook)

            Wqkv_hook.block_inx = block_id
            Wqkv_hook.branch_inx = branch_idx
            proj_hook.block_inx = block_id
            proj_hook.branch_inx = branch_idx

        for idx, block in enumerate(self.transformer.core_block, start=1):
            xk, attn_map = block(xk, freqs_cis, block_idx + idx, mask, past_key_values, return_attn=return_attn)
            attn_maps[block_idx + idx] = attn_map

        for bid, block in enumerate(self.transformer.core_block):
            Wqkv_hook = list(block.attn.Wqkv._forward_hooks.values())[0]
            proj_hook = list(block.attn.proj._forward_hooks.values())[0]

            Wqkv_hook.block_inx = None
            Wqkv_hook.branch_inx = None
            proj_hook.block_inx = None
            proj_hook.branch_inx = None

        return xk, block_idx + idx, attn_maps

    def core_block_forward_lora(
        self,
        x,
        input_embeds,
        branch_idx,
        freqs_cis,
        mask,
        past_key_values,
        block_idx: Union[torch.Tensor, int],
        attn_maps: dict = {},
        return_attn: bool = False,
    ):
        xk = self.transformer.adapter(torch.cat([x, input_embeds.to(x.device)], dim=-1))
        for bid, block in enumerate(self.transformer.core_block):
            Wqkv_hook = list(block.attn.Wqkv._forward_hooks.values())[0]
            proj_hook = list(block.attn.proj._forward_hooks.values())[0]

            assert isinstance(Wqkv_hook, LoRAHook)
            assert isinstance(proj_hook, LoRAHook)

            Wqkv_hook.block_inx = bid
            Wqkv_hook.branch_inx = branch_idx

            proj_hook.block_inx = bid
            proj_hook.branch_inx = branch_idx

        for idx, block in enumerate(self.transformer.core_block, start=1):
            xk, attn_map = block(xk, freqs_cis, block_idx + idx, mask, past_key_values, return_attn=return_attn)
            attn_maps[block_idx + idx] = attn_map

        for bid, block in enumerate(self.transformer.core_block):

            Wqkv_hook = list(block.attn.Wqkv._forward_hooks.values())[0]
            proj_hook = list(block.attn.proj._forward_hooks.values())[0]

            assert isinstance(Wqkv_hook, LoRAHook)
            assert isinstance(proj_hook, LoRAHook)

            Wqkv_hook.block_inx = None
            Wqkv_hook.branch_idx = None
            proj_hook.block_inx = None
            proj_hook.branch_idx = None

        return xk, block_idx + idx, attn_maps

    def route_core_block_forward(
        self,
        x,
        topk_idx,
        topk_weight,
        input_embeds,
        freqs_cis,
        mask,
        past_key_values,
        block_idx: Union[torch.Tensor, int],
        attn_maps: dict = {},
        return_attn: bool = False,
    ):
        orig_shape = x.shape # [bsz, seq_len, h]
        flat_topk_idx = topk_idx.view(-1) # [bsz * topk]

        hidden_states = x.repeat_interleave(self.config.num_branches_per_tok, dim=0) # [topk, bsz, seq_len, h]
        input_embeds = input_embeds.repeat_interleave(self.config.num_branches_per_tok, dim=0)  # [topk, bsz, seq_len, h]
        if mask is not None:
            mask = mask.repeat_interleave(self.config.num_branches_per_tok, dim=0) # [topk, bsz, seq_len]

        y = torch.zeros_like(hidden_states)
        return_block_idx = None
        for branch_idx in range(self.config.num_branches):
            if branch_idx not in flat_topk_idx:
                continue

            tmp_block_idx = block_idx
            if mask is not None:
                mask_ = mask[flat_topk_idx == branch_idx]
            else:
                mask_ = None
            x = hidden_states[flat_topk_idx == branch_idx]
            sub_input_embeds = input_embeds[flat_topk_idx == branch_idx]

            x, tmp_block_idx, attn_maps = self.core_block_forward(
                x = x,
                input_embeds = sub_input_embeds,
                branch_idx = branch_idx,
                freqs_cis = freqs_cis,
                mask = mask_,
                past_key_values = past_key_values,
                block_idx = tmp_block_idx,
                attn_maps = attn_maps,
                return_attn = return_attn
            )

            y[flat_topk_idx == branch_idx] = x
            if return_block_idx is None:
                return_block_idx = tmp_block_idx

        if self.config.router_type == "gate" and (self.training or y.shape[0] > 1):
            y = (y.view(*topk_weight.shape, orig_shape[1], -1) * topk_weight.unsqueeze(-1).unsqueeze(-1)).sum(1)
        else:
            y = y.view(*orig_shape)

        return y, return_block_idx, attn_maps

    @torch.no_grad()
    def iterate_one_step(
        self,
        input_embeds,
        input_states,
        position_ids: Optional[torch.Tensor] = None,
        cache_position: Optional[torch.Tensor] = None,
        block_idx: Union[torch.Tensor, int] = 0,
        attention_mask: Optional[Tensor] = None,
        past_key_values: Optional[Cache] = None,
        attn_maps: dict = {},
    ):
        if position_ids is None and cache_position is None:
            freqs_cis = self.freqs_cis[:, : input_embeds.shape[1]]
        elif position_ids is not None:
            freqs_cis = self.freqs_cis.index_select(1, position_ids.squeeze())
        elif cache_position is not None:
            freqs_cis = self.freqs_cis[:, cache_position]
        x, block_idx, attn_maps = self.core_block_forward(
            input_states, input_embeds, freqs_cis, attention_mask, past_key_values, block_idx, attn_maps
        )
        return x, block_idx, attn_maps

    def predict_from_latents(
        self,
        latents,
        attention_mask: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.Tensor] = None,
        cache_position: Optional[torch.Tensor] = None,
        past_key_values: Optional[Cache] = None,
        return_attn: bool = False,
        attn_maps: dict = {},
    ):
        if position_ids is None and cache_position is None:
            freqs_cis = self.freqs_cis[:, : latents.shape[1]]
        elif position_ids is not None:
            freqs_cis = self.freqs_cis.index_select(1, position_ids.squeeze())
        elif cache_position is not None:
            freqs_cis = self.freqs_cis[:, cache_position]
        x = self.transformer.ln_f(latents)
        # Coda layers
        for block_idx, block in enumerate(self.transformer.coda, start=1):
            x, attn_map = block(x, freqs_cis, -block_idx, attention_mask, past_key_values)
        attn_maps[block_idx] = attn_map
        x = self.transformer.ln_f(x)

        logits = self.lm_head(x).float()

        return CausalLMOutputRecurrentLatents(
            loss=torch.as_tensor(0.0),
            log_ppl=torch.as_tensor(0.0),
            logits=logits,
            past_key_values=past_key_values,
            attention_maps=attn_maps if len(attn_maps) > 0 else None,
        )

    def embed_inputs(
        self,
        input_ids: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.Tensor] = None,
        past_key_values: Optional[Cache] = None,
        use_cache: bool = False,
        cache_position: Optional[torch.Tensor] = None,
        return_attn: bool = False,
        **kwargs,
    ) -> tuple[torch.Tensor, int, dict[int, Tensor]]:
        # Support multiple position formats:
        if position_ids is None and cache_position is None:
            freqs_cis = self.freqs_cis[:, : input_ids.shape[1]]
        elif position_ids is not None:
            freqs_cis = self.freqs_cis.index_select(1, position_ids.squeeze())
        elif cache_position is not None:
            freqs_cis = self.freqs_cis[:, cache_position]

        input_embeds = self.transformer.wte(input_ids)

        if self.emb_scale != 1:
            input_embeds = input_embeds * self.emb_scale  # type: ignore

        if use_cache and past_key_values is None:
            past_key_values = HuginnDynamicCache()

        # Non-recurrent prelude
        attn_maps = {}
        for block_idx, block in enumerate(self.transformer.prelude):
            input_embeds, attn_maps = block(
                input_embeds, freqs_cis, block_idx, attention_mask, past_key_values, return_attn
            )
        return input_embeds, block_idx, attn_maps

    @torch._dynamo.disable(recursive=False)  # type: ignore
    def randomized_iteration_sampler(self) -> tuple[torch.Tensor, torch.Tensor]:
        """Outputs are long tensors so that they can be passed through compiled functions"""
        t = max(self.config.mean_recurrence - self.config.mean_backprop_depth, 0)
        s = self.config.mean_backprop_depth
        if torch.rand((1,)).is_meta:  # annoying clause to make meta-tensor-based flop counting work
            # these values are only the mean TFLOPs of the randomized sampler
            # Note that this clause also breaks the contract, and returns ints in meta tensor mode
            return t, s  # type: ignore
        if self.training:
            sigma = 0.5
            mu = math.log(t + s) - (sigma**2 / 2)
            rate = torch.zeros((1,)).log_normal_(mean=mu, std=sigma)
            p = torch.poisson(torch.tensor([rate], dtype=torch.float)) + 1
            n = torch.clamp(p - s, min=0)
            k = torch.as_tensor(torch.minimum(torch.as_tensor(s), p))
        else:
            n, k = torch.as_tensor(self.config.mean_recurrence), torch.as_tensor(0)

        return n.to(dtype=torch.long), k.to(dtype=torch.long)

    def initialize_state(self, input_embeds, deterministic: bool = False):
        x = torch.randn_like(input_embeds)
        std = self.config.init_values["std"]
        torch.nn.init.trunc_normal_(x, mean=0.0, std=std, a=-3 * std, b=3 * std)
        if self.emb_scale != 1:
            x = x * self.emb_scale
        return x if not deterministic else x.zero_()

    def prepare_inputs_for_generation(
        self,
        input_ids: torch.LongTensor,
        past_key_values: Optional[Cache] = None,
        attention_mask: Optional[torch.LongTensor] = None,
        inputs_embeds: Optional[torch.FloatTensor] = None,
        cache_position: Optional[torch.LongTensor] = None,
        **kwargs,
    ):
        model_inputs = {}
        model_inputs["cache_position"] = cache_position
        current_input_length = input_ids.shape[1]
        if past_key_values is not None:
            if type(past_key_values) != HuginnDynamicCache:
                # Need to use custom cache, detect and replace HF dynamic cache if generate injects it
                assert past_key_values.get_seq_length() == 0
                past_key_values = HuginnDynamicCache()
            model_inputs["past_key_values"] = past_key_values if kwargs["use_cache"] else None
            input_ids = input_ids[:, cache_position]  # type: ignore
        model_inputs["input_ids"] = input_ids.clone(memory_format=torch.contiguous_format)

        if cache_position is None:
            position_ids = torch.arange(current_input_length)[None, :].to(input_ids.device)
            model_inputs["position_ids"] = position_ids[:, -current_input_length:].clone(
                memory_format=torch.contiguous_format
            )  # some form of position_ids is a critical argument for the model to correctly apply rope!

        # forward all other entries
        for key, value in kwargs.items():
            if key not in model_inputs:
                model_inputs[key] = value
        return model_inputs

    @torch.no_grad()
    def generate(self, *args, **kwargs):
        """Dispatcher - use HF generate in all normal cases.
        If BOTH `criterion` AND `exit_threshold` are provided as not None, we use adaptive compute.
        """
        self.trajectory_choice_idx = []
        if kwargs.get("criterion", None) is not None and kwargs.get("exit_threshold", None) is not None:
            print("Dispatching to custom generate function call")
            return self.generate_with_adaptive_compute(*args, **kwargs)
        else:
            return super().generate(*args, **kwargs)

    @torch.no_grad()
    def generate_minimal(
        self,
        input_ids: torch.LongTensor,
        generation_config: Optional[GenerationConfig] = None,  # type: ignore
        tokenizer=None,
        streamer=None,
        continuous_compute=False,  # warm-start state / continuous CoT
        cache_kwargs: dict = {},
        **model_kwargs,
    ) -> Union[torch.Tensor, dict[str, Any]]:
        """Minimal single-sequence generation. Template for more complicated generate tasks"""
        # Setup
        if generation_config is None:
            generation_config: GenerationConfig = self.generation_config  # type: ignore
        model_kwargs["past_key_values"] = HuginnDynamicCache(**cache_kwargs)
        model_kwargs["use_cache"] = True
        model_kwargs = self._get_initial_cache_position(input_ids, model_kwargs)
        stop_tokens = self._get_stops(generation_config, tokenizer).to(input_ids.device)
        if continuous_compute:
            embedded_inputs, _, _ = self.embed_inputs(input_ids)
            model_kwargs["input_states"] = self.initialize_state(embedded_inputs)
        # Generate tokens
        for _ in range(generation_config.max_length - input_ids.shape[1]):
            # Forward pass
            model_inputs = self.prepare_inputs_for_generation(input_ids, **model_kwargs)
            outputs = self(**model_inputs)
            next_token_logits = outputs.logits[0, -1, :]
            if continuous_compute:
                current_last_latent = outputs.latent_states[:, -1:, :]

            # Sample or select next token
            if generation_config.do_sample:
                if generation_config.temperature:
                    next_token_logits = next_token_logits / generation_config.temperature

                probs = F.softmax(next_token_logits, dim=-1)

                # Apply top_k
                if generation_config.top_k:
                    top_k_probs, _ = torch.topk(probs, generation_config.top_k)
                    probs[probs < top_k_probs[-1]] = 0
                # Apply top_p
                if generation_config.top_p:
                    sorted_probs = torch.sort(probs, descending=True)[0]
                    cumsum = torch.cumsum(sorted_probs, dim=-1)
                    probs[cumsum > generation_config.top_p] = 0
                # Apply min_p
                if generation_config.min_p:
                    probs[probs < generation_config.min_p * probs.max()] = 0

                probs = probs / probs.sum()
                next_token = torch.multinomial(probs, num_samples=1)
            else:
                next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)

            input_ids = torch.cat([input_ids, next_token[None, :]], dim=-1)  # type: ignore

            if streamer:
                streamer.put(next_token.cpu())

            # Update model kwargs
            model_kwargs = self._update_model_kwargs_for_generation(outputs, model_kwargs)
            if continuous_compute:
                model_kwargs["input_states"] = current_last_latent

            # Check if we hit a stop token
            if stop_tokens is not None and next_token in stop_tokens:
                break

        if streamer:
            streamer.end()

        if generation_config.return_dict_in_generate:
            return GenerateDecoderOnlyOutput(
                sequences=input_ids,
                scores=None,
                logits=None,
                attentions=None,
                hidden_states=None,
                past_key_values=model_kwargs.get("past_key_values"),
            )
        return input_ids

    @torch.no_grad()
    def generate_with_adaptive_compute(
        self,
        input_ids: torch.LongTensor,
        generation_config: Optional[GenerationConfig] = None,  # type: ignore
        tokenizer=None,
        streamer=None,
        continuous_compute=False,  # warm-start state / continuous CoT
        latent_dampening=False,
        criterion="entropy-diff",
        exit_threshold: Union[str, float, int] = "auto",
        cache_kwargs: dict = {},
        **model_kwargs,
    ) -> Union[torch.Tensor, GenerateDecoderOnlyOutput]:
        """
        Generate tokens with adaptive compute. This is NOT the most efficient implementation.
        For batches, on each token, we iterate until the entire batch finishes.
        """
        # Setup
        if generation_config is None:
            generation_config: GenerationConfig = self.generation_config  # type: ignore
        model_kwargs["past_key_values"] = HuginnDynamicCache(**cache_kwargs)
        model_kwargs["use_cache"] = True
        model_kwargs = self._get_initial_cache_position(input_ids, model_kwargs)
        stop_tokens = self._get_stops(generation_config, tokenizer).to(input_ids.device)
        batch_size = input_ids.shape[0]
        compute_steps = []

        # Set up continuous compute if enabled
        if continuous_compute:
            embedded_inputs, _, _ = self.embed_inputs(input_ids)
            current_last_latents = self.initialize_state(embedded_inputs)

        # Track which sequences have finished
        finished_sequences = torch.zeros(batch_size, dtype=torch.bool, device=input_ids.device)

        # Generate tokens
        for step in range(generation_config.max_length - input_ids.shape[1]):
            # Adaptive compute forward
            model_inputs = self.prepare_inputs_for_generation(input_ids, **model_kwargs)
            aux_inputs = {
                k: model_inputs[k] for k in ["cache_position", "past_key_values", "attention_mask"] if k in model_inputs
            }
            embedded_inputs, block_idx, _ = self.embed_inputs(model_inputs["input_ids"], **aux_inputs)
            if not continuous_compute:
                current_latents = self.initialize_state(embedded_inputs, deterministic=False)
            else:
                current_latents = current_last_latents

            # Initialize criterion tracking for each sequence in batch
            exit_values_per_seq = [[] for _ in range(batch_size)]
            compute_steps_per_seq = [0] * batch_size
            exit_reached = torch.zeros(batch_size, dtype=torch.bool, device=input_ids.device)

            # Set up criterions based on selected strategy
            if criterion == "entropy-diff":
                entropy = torch.ones(batch_size, device=input_ids.device) * 100.0
                exit_threshold = 1e-3 if exit_threshold == "auto" else float(exit_threshold)
            elif criterion in ["latent-diff", "none"]:
                exit_threshold = 0.03 if exit_threshold == "auto" else float(exit_threshold)
            elif "kl" in criterion:
                V = self.config.padded_vocab_size
                log_probs = ((1 / V) * torch.ones(batch_size, V, device=input_ids.device)).log()
                if criterion == "minp-kl":
                    exit_threshold = 1e-6 if exit_threshold == "auto" else float(exit_threshold)
                else:
                    exit_threshold = 5e-4 if exit_threshold == "auto" else float(exit_threshold)
            elif criterion == "argmax-stability":
                stable_for_n_steps = torch.zeros(batch_size, dtype=torch.long, device=input_ids.device)
                current_argmax = torch.ones(batch_size, dtype=torch.long, device=input_ids.device) * -1
                exit_threshold = 5 if exit_threshold == "auto" else int(exit_threshold)
            else:
                raise ValueError("Invalid adaptive compute strategy.")

            all_latents = []
            next_token_logits = None

            # Iterate through compute steps
            for compute_step in range(model_inputs["num_steps"]):
                prev_latents = current_latents.clone()
                current_latents, block_idx, _ = self.iterate_one_step(
                    embedded_inputs, current_latents, block_idx=block_idx, **aux_inputs
                )

                if latent_dampening:
                    all_latents.append(current_latents)

                if step > 0:  # do not exit in prefill:
                    # Check exit condition for each sequence in batch
                    if criterion == "entropy-diff":
                        prev_entropy = entropy
                        outputs = self.predict_from_latents(current_latents, **aux_inputs)
                        logits: torch.Tensor = outputs.logits  # type: ignore
                        probs = F.softmax(logits[:, -1, :], dim=-1)
                        entropy = -torch.sum(probs * torch.log(probs + 1e-10), dim=-1)
                        exit_values = (entropy - prev_entropy).abs()

                    elif criterion == "latent-diff":
                        norm_diff = (prev_latents - current_latents).norm(dim=-1) / current_latents.norm(dim=-1)
                        exit_values = norm_diff.mean(dim=-1)

                    elif "kl" in criterion:
                        outputs = self.predict_from_latents(current_latents, **aux_inputs)
                        logits: torch.Tensor = outputs.logits  # type: ignore
                        prev_log_probs = log_probs
                        if criterion == "minp-kl":
                            probs = F.softmax(logits[:, -1, :], dim=-1)
                            max_probs = probs.max(dim=-1, keepdim=True)[0]
                            probs_mask = probs < (0.1 * max_probs)
                            masked_probs = probs
                            masked_probs[probs_mask] = 1 / V
                            probs = masked_probs / masked_probs.sum(dim=-1, keepdim=True)
                            log_probs = probs.log()
                        else:
                            log_probs = F.log_softmax(logits[:, -1, :], dim=-1)
                        exit_values = F.kl_div(log_probs, prev_log_probs, reduction="none", log_target=True).sum(dim=-1)

                    elif criterion == "argmax-stability":
                        prev_argmax = current_argmax
                        outputs = self.predict_from_latents(current_latents, **aux_inputs)
                        logits: torch.Tensor = outputs.logits  # type: ignore
                        current_argmax = logits[:, -1, :].argmax(dim=-1)
                        stable_for_n_steps = torch.where(
                            current_argmax == prev_argmax, stable_for_n_steps + 1, torch.zeros_like(stable_for_n_steps)
                        )
                        exit_values = stable_for_n_steps

                    # Record values and check exits for each sequence
                    for i in range(batch_size):
                        if not exit_reached[i] and not finished_sequences[i]:
                            exit_values_per_seq[i].append(exit_values[i].item())

                    new_exits = (
                        exit_values < exit_threshold
                        if criterion != "argmax-stability"
                        else exit_values >= exit_threshold
                    )
                    new_exits = new_exits & ~exit_reached & ~finished_sequences

                    if new_exits.any():
                        exit_reached = exit_reached | new_exits
                        if criterion == "latent-diff":
                            # Normally we don't compute the output for latent-diff, but when there is an exit,
                            # we need to compute and save the output
                            outputs = self.predict_from_latents(current_latents, **aux_inputs)
                            logits: torch.Tensor = outputs.logits  # type: ignore
                        if next_token_logits is None:
                            next_token_logits = logits[:, -1, :].clone()
                        else:
                            next_token_logits = torch.where(
                                new_exits.unsqueeze(1).expand_as(logits[:, -1, :]), logits[:, -1, :], next_token_logits
                            )
                        for i in range(batch_size):
                            if new_exits[i]:
                                compute_steps_per_seq[i] = compute_step + 1

                    # If all sequences have exited, break early
                    if (exit_reached | finished_sequences).all():
                        break
            # This else is if the for loop finished without breaking
            else:
                if not latent_dampening:
                    outputs = self.predict_from_latents(current_latents, **aux_inputs)
                else:
                    dampened_latents = torch.sum(torch.cat(all_latents, dim=0), dim=0, keepdim=True)
                    outputs = self.predict_from_latents(dampened_latents, **aux_inputs)

                # For sequences that didn't exit early, use the final logits
                if next_token_logits is None:
                    next_token_logits = outputs.logits[:, -1, :]  # type: ignore
                else:
                    # Only update logits for sequences that didn't exit early
                    non_exit_mask = ~exit_reached & ~finished_sequences
                    next_token_logits = torch.where(
                        non_exit_mask.unsqueeze(1).expand_as(next_token_logits),
                        outputs.logits[:, -1, :],  # type: ignore
                        next_token_logits,
                    )

                    # Record compute steps for non-exited sequences
                    for i in range(batch_size):
                        if non_exit_mask[i]:
                            compute_steps_per_seq[i] = model_inputs["num_steps"]

            # Save latent states for continuous compute if enabled
            if continuous_compute:
                current_last_latents = current_latents[:, -1:, :]

            # Record compute steps for this token generation
            compute_steps.append([compute_steps_per_seq, exit_values_per_seq])

            # Sample or select next token based on generation config
            if generation_config.do_sample:
                next_token = self._sample_next_token(
                    next_token_logits,
                    generation_config.temperature,
                    generation_config.top_k,
                    generation_config.top_p,
                    generation_config.min_p,
                )
            else:
                next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)  # type: ignore

            input_ids = torch.cat([input_ids, next_token], dim=-1)  # type: ignore

            if streamer:
                streamer.put(next_token.cpu())

            # Update model kwargs
            model_kwargs = self._update_model_kwargs_for_generation(outputs, model_kwargs)
            if continuous_compute:
                model_kwargs["input_states"] = current_last_latents

            # Check for finished sequences
            for i in range(batch_size):
                if not finished_sequences[i] and stop_tokens is not None and next_token[i, 0] in stop_tokens:
                    finished_sequences[i] = True

            # Break if all sequences are finished
            if finished_sequences.all():
                break

        if streamer:
            streamer.end()

        if generation_config.return_dict_in_generate:
            return GenerateDecoderOnlyOutput(
                sequences=input_ids,
                scores=compute_steps,  # type: ignore
                logits=None,
                attentions=None,
                hidden_states=None,
                past_key_values=model_kwargs.get("past_key_values"),
            )
        return input_ids

    def _get_stops(self, generation_config, tokenizer):
        stop_tokens = set()
        if generation_config.eos_token_id is not None:
            stop_tokens.add(generation_config.eos_token_id)
        if hasattr(generation_config, "stop_strings") and tokenizer and generation_config.stop_strings:
            for s in generation_config.stop_strings:
                token_id = tokenizer(s, add_special_tokens=False)["input_ids"][0]
                stop_tokens.add(token_id)
        return torch.tensor(list(stop_tokens))

    def _sample_next_token(self, next_token_logits, temperature=None, top_k=None, top_p=None, min_p=None):
        """Helper function to sample the next token."""
        if temperature:
            next_token_logits = next_token_logits / temperature

        probs = F.softmax(next_token_logits, dim=-1)

        # Apply top_k
        if top_k:
            top_k_values, _ = torch.topk(probs, top_k, dim=-1)
            min_values = top_k_values[:, -1].unsqueeze(-1).expand_as(probs)
            probs = torch.where(probs < min_values, torch.zeros_like(probs), probs)

        # Apply top_p (nucleus sampling)
        if top_p:
            sorted_probs, sorted_indices = torch.sort(probs, descending=True, dim=-1)
            cumulative_probs = torch.cumsum(sorted_probs, dim=-1)

            # Create mask for probs to keep
            remove_indices = cumulative_probs > top_p
            remove_indices[:, 0] = False  # Keep at least the top probability

            # Convert sorted indices mask back to original indices mask
            mask = torch.zeros_like(probs, dtype=torch.bool)
            for i in range(probs.shape[0]):
                mask[i, sorted_indices[i, remove_indices[i]]] = True

            probs = torch.where(mask, torch.zeros_like(probs), probs)

        # Apply min_p
        if min_p:
            max_probs = probs.max(dim=-1, keepdim=True)[0]
            min_p_threshold = min_p * max_probs
            probs = torch.where(probs < min_p_threshold, torch.zeros_like(probs), probs)

        # Renormalize probabilities
        probs = probs / probs.sum(dim=-1, keepdim=True).clamp(min=1e-10)

        # Sample from the distribution
        next_token = torch.multinomial(probs, num_samples=1)
        return next_token

    def get_stats(self, logits, x, latent_states, xk, input_embeds, num_steps_no_grad, num_steps_with_grad):
        probs = torch.softmax(logits.float(), dim=-1)
        prob_entropy = torch.where(probs > 0, -probs * probs.log(), 0).sum(dim=-1)
        residual_diff = (x - latent_states).norm(dim=-1)
        rel_residual = residual_diff / latent_states.norm(dim=-1)
        stats = {
            "entropy": prob_entropy,
            "residual_diff": residual_diff,
            "rel_residual": rel_residual,
            "num_steps_no_grad": num_steps_no_grad,
            "num_steps_with_grad": num_steps_with_grad,
        }
        return stats


#################################### Utils #######################################################################
def precompute_freqs_cis(dim: int, end: int, theta: float = 10000.0, condense_ratio: int = 1):
    with torch.autocast("cuda", enabled=False):
        inv_freqs = 1.0 / (theta ** (torch.arange(0, dim, 2, dtype=torch.float32) / dim))
        t = torch.arange(end, dtype=torch.float32, device=inv_freqs.device) / condense_ratio
        freqs = torch.outer(t, inv_freqs).float()
        return torch.stack([torch.cos(freqs)[None, :, None, :], torch.sin(freqs)[None, :, None, :]], dim=4)
        # equivalent to
        # freqs_cis = torch.polar(torch.ones_like(freqs), freqs)
        # cache = torch.stack([freqs_cis.real, freqs_cis.imag], dim=-1)


def apply_rotary_emb_complex_like(q: Tensor, k: Tensor, freqs_cis: Tensor) -> tuple[Tensor, Tensor]:
    with torch.autocast("cuda", enabled=False):
        qk_r2 = torch.cat([q, k], dim=2).unflatten(dim=-1, sizes=(-1, 2)).float()  # cast to float32 for smooth skin
        rotated_qk_r2 = torch.stack(
            [
                qk_r2[..., 0] * freqs_cis[..., 0] - qk_r2[..., 1] * freqs_cis[..., 1],
                qk_r2[..., 1] * freqs_cis[..., 0] + qk_r2[..., 0] * freqs_cis[..., 1],
            ],
            -1,
        ).flatten(3)
        rotated_qk = rotated_qk_r2
        return torch.split(rotated_qk.type_as(q), q.shape[2], dim=2)  # type: ignore


#################################### HF registration ############################################################

from transformers import AutoConfig, AutoModel, AutoModelForCausalLM

# New
RavenConfig.register_for_auto_class()

RavenForCausalLM.register_for_auto_class("AutoModel")
RavenForCausalLM.register_for_auto_class("AutoModelForCausalLM")

# Old?
AutoConfig.register("huginn_raven", RavenConfig)
AutoModel.register(RavenConfig, RavenForCausalLM)
AutoModelForCausalLM.register(RavenConfig, RavenForCausalLM)