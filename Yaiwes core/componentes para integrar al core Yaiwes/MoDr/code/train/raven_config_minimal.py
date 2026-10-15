"""A HuggingFace-style model configuration."""

from transformers import PretrainedConfig
from math import sqrt


class RavenConfig(PretrainedConfig):
    r"""
    This is the configuration class for the Raven model, inheriting from HuggingFace's PretrainedConfig.

    Args:
        n_embd (`int`, *optional*, defaults to 5280):
            The embedding dimension of the model.
        n_heads (`int`, *optional*, defaults to 55):
            Number of attention heads in the model.
        n_layers (`int`, *optional*, defaults to 8):
            Total number of layers, including prelude, recurrent, and coda layers.
        block_size (`int`, *optional*, defaults to 4096):
            Maximum sequence length that this model might ever be used with.
        vocab_size (`int`, *optional*, defaults to 65536):
            Vocabulary size of the model. Defines the number of different tokens that can be represented.
        padding_multiple (`int`, *optional*, defaults to 4096):
            The multiple by which to pad the vocabulary size.
        tie_embeddings (`bool`, *optional*, defaults to True):
            Whether the input and output embeddings should be tied.
        intermediate_size (`int`, *optional*, defaults to 17920):
            Dimensionality of the intermediate MLP layers.
        bias (`bool`, *optional*, defaults to False):
            Whether to use bias terms in linear layers.
        architecture_class_name (`str`, *optional*, defaults to "RecurrentGPT"):
            Name of the main architecture class to use.
        block_class_name (`str`, *optional*, defaults to "SandwichBlock"):
            Type of transformer block implementation to use.
        norm_class_name (`str`, *optional*, defaults to "RMSNorm_llama"):
            Type of normalization layer to use.
        norm_eps (`float`, *optional*, defaults to 1e-6):
            The epsilon value used in the normalization layers.
        mlp_class_name (`str`, *optional*, defaults to "GatedMLP"):
            Type of MLP implementation to use.
        nonlin_name (`str`, *optional*, defaults to "SiLU"):
            Name of the activation function to use.
        init_strategy (`str`, *optional*, defaults to "takase"):
            Strategy to use for weight initialization.
        init_orthogonal (`bool`, *optional*, defaults to False):
            Whether to use orthogonal initialization for weights.
        state_init (`str`, *optional*, defaults to "like-init"):
            Method for initializing recurrent states.
        injection_type (`str`, *optional*, defaults to "linear"):
            Type of state injection mechanism to use.
        n_layers_in_recurrent_block (`int`, *optional*, defaults to 4):
            Number of layers within each recurrent block.
        mean_recurrence (`int`, *optional*, defaults to 32):
            Expected number of recurrences in the model.
        sampling_scheme (`str`, *optional*, defaults to "poisson-lognormal-filling"):
            Scheme used for sampling recurrence depths.
        mean_backprop_depth (`int`, *optional*, defaults to 8):
            Mean depth for backpropagation through time.
        n_layers_in_prelude (`int`, *optional*, defaults to 2):
            Number of layers in the prelude section.
        n_layers_in_coda (`int`, *optional*, defaults to 2):
            Number of layers in the coda section.
        qk_bias (`bool`, *optional*, defaults to True):
            Whether to use bias in query-key attention computations.
        activation_checkpoint_impl (`str`, *optional*, defaults to "per-iteration"):
            Implementation strategy for activation checkpointing.
        rope_base (`float`, *optional*, defaults to 50000):
            Base value for rotary position embeddings.
        torch_dtype (`str`, *optional*, defaults to "bfloat16"):
            Default torch dtype for the model.
        num_branches_per_tok (`int`, *optional*, defaults to 1):
            Number of branches to be selected per token.
        num_branche (`int`, *optional*, defaults to 3):
            Number of branch networks in the model.
        num_choices (`int`, *optional*, defaults to 3):
            Number of times a branch network switches paths.
        per_branch_depth (`int`, *optional*, defaults to 3):
            Number of block in each branch network.
        scoring_func (`str`, *optional*, defaults to "sigmoid"):
            Function used for branch scoring.
        routed_scaling_factor (`float`, *optional*, defaults to 2.5):
            Scaling factor for the routed logits.
        aux_loss_alpha (`float`, *optional*, defaults to 0.001):
            Weight for the auxiliary loss in branch routing.
        seq_aux (`bool`, *optional*, defaults to True):
            Whether to use sequence-level auxiliary loss.
        norm_topk_prob (`bool`, *optional*, defaults to True):
            Whether to normalize top-k probabilities.
        topk_method (`str`, *optional*, defaults to "noaux_tc"):
            Method used for top-k selection in branch routing.
        n_group (`int`, *optional*, defaults to 1):
            Number of groups for grouped branch routing.
        topk_group (`int`, *optional*, defaults to 1):
            Number of top-k selections per group.
    """

    model_type = "huginn_raven"
    keys_to_ignore_at_inference = [""]
    attribute_map = {"num_attention_heads": "n_heads", "hidden_size": "n_embd", "num_hidden_layers": "n_layers"}

    def __init__(
        self,
        n_embd: int = 5280,
        n_heads: int = 55,
        n_layers: int = 8,  # total of prelude + recurrent + coda
        block_size: int = 4096,
        vocab_size: int = 65536,
        padding_multiple: int = 4096,
        tie_embeddings: bool = True,
        intermediate_size: int = 17920,
        bias: bool = False,
        architecture_class_name: str = "RecurrentGPT",
        block_class_name: str = "SandwichBlock",
        norm_class_name: str = "RMSNorm_llama",
        norm_eps: float = 0.000001,
        mlp_class_name: str = "GatedMLP",
        nonlin_name: str = "SiLU",
        init_strategy: str = "takase",
        init_orthogonal: bool = False,
        state_init: str = "like-init",
        injection_type: str = "linear",
        n_layers_in_recurrent_block: int = 4,
        mean_recurrence: int = 32,
        sampling_scheme: str = "poisson-lognormal-filling",
        mean_backprop_depth: int = 8,
        n_layers_in_prelude: int = 2,
        n_layers_in_coda: int = 2,
        qk_bias: bool = True,
        activation_checkpoint_impl: str = "per-iteration",
        rope_base: float = 50_000,
        torch_dtype: str = "bfloat16",
        router_type: str = 'gate',
        fine_tuning_algorithm: str = None,
        svd_cache_file: str = './decompose_tensor.pt',
        target_modules  =  (
            "transformer.core_block.0.attn.Wqkv",
            "transformer.core_block.0.attn.proj",
            "transformer.core_block.1.attn.Wqkv",
            "transformer.core_block.1.attn.proj",
            "transformer.core_block.2.attn.Wqkv",
            "transformer.core_block.2.attn.proj",
            "transformer.core_block.3.attn.Wqkv",
            "transformer.core_block.3.attn.proj",
        ),
        lora_r: int = 16,
        lora_alpha: int = 16,
        num_branches: int = 3,
        num_steps: tuple[int, int] = None,
        num_branches_per_tok: int = 1,
        num_choices: int = 3,
        per_branch_depth: int = 3,
        scoring_func: str = "softmax",
        routed_scaling_factor: float = 2.5,
        aux_loss_alpha: float = 0.01,
        update_rate: float = 1e-4,
        seq_aux: bool = False,
        norm_topk_prob: bool = True,
        topk_method: str = 'greedy',
        n_group: int = 1,
        topk_group: int = 1,
        # router_infer_horizon: int = 10,
        transformers_version: str = "4.47.1",
        **kwargs,
    ):
        self.n_embd = n_embd
        self.n_heads = n_heads
        self.n_layers = n_layers
        self.block_size = block_size
        self.vocab_size = self.padded_vocab_size = vocab_size
        self.padding_multiple = padding_multiple
        self.tie_embeddings = tie_embeddings
        self.intermediate_size = intermediate_size
        self.bias = bias
        self.architecture_class_name = architecture_class_name
        self.block_class_name = block_class_name
        self.norm_class_name = norm_class_name
        self.norm_eps = norm_eps
        self.mlp_class_name = mlp_class_name
        self.nonlin_name = nonlin_name
        self.init_strategy = init_strategy
        self.init_orthogonal = init_orthogonal
        self.state_init = state_init
        self.injection_type = injection_type
        self.n_layers_in_recurrent_block = n_layers_in_recurrent_block
        self.mean_recurrence = mean_recurrence
        self.sampling_scheme = sampling_scheme
        self.mean_backprop_depth = mean_backprop_depth
        self.n_layers_in_prelude = n_layers_in_prelude
        self.n_layers_in_coda = n_layers_in_coda
        self.qk_bias = qk_bias
        self.activation_checkpoint_impl = activation_checkpoint_impl
        self.rope_base = rope_base
        self.torch_dtype = torch_dtype  # Added from JSON
        self.transformers_version = transformers_version  # Added from JSON
        # Derived
        self.num_key_value_heads = n_heads
        self.num_attention_heads = n_heads
        self.head_dim = n_embd // n_heads
        self.effective_expected_depth = (
            self.n_layers_in_prelude + self.n_layers_in_coda + self.n_layers_in_recurrent_block * self.mean_recurrence
        )
        self.router_type = router_type
        self.svd_cache_file = svd_cache_file
        self.num_branches = num_branches
        self.num_steps = num_steps
        self.init_values = {
            "std": sqrt(2 / (5 * self.n_embd)),
            "out_proj": sqrt(2 / (5 * self.n_embd)) / sqrt(2 * self.effective_expected_depth),
            "embedding": sqrt(2 / (5 * self.n_embd)),
            "embed_scale": sqrt(self.n_embd),
        }
        # Router
        self.num_branches_per_tok = num_branches_per_tok
        self.num_choices = num_choices
        self.per_branch_depth = per_branch_depth
        self.fine_tuning_algorithm = fine_tuning_algorithm
        self.target_modules = target_modules
        self.lora_r = lora_r
        self.lora_alpha = lora_alpha
        self.scoring_func = scoring_func
        self.routed_scaling_factor = routed_scaling_factor
        self.aux_loss_alpha = aux_loss_alpha
        self.update_rate = update_rate
        self.seq_aux = seq_aux
        self.norm_topk_prob = norm_topk_prob
        self.topk_method = topk_method
        self.n_group = n_group
        self.topk_group = topk_group
        # self.router_infer_horizon = router_infer_horizon
        self.router_choice_idx = None
        super().__init__(
            # pad_token_id=65509,
            # bos_token_id=65504,
            # eos_token_id=65505,
            tie_word_embeddings=tie_embeddings,
            **kwargs,
        )