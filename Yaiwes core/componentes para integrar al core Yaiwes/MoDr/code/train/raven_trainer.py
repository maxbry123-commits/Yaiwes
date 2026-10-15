import torch
import numpy as np
from transformers import Trainer
from torch import distributed as dist
from torch.utils.data.distributed import DistributedSampler
from transformers import is_wandb_available
from collections import Counter
import math

if is_wandb_available():
    import wandb

class RavenTrainer(Trainer):

    def __init__(self, *args, **kwargs):
        self.custom_bos_token = kwargs.pop("custom_bos_token", "<|begin_resp|>")
        super().__init__(*args, **kwargs)

    def generate_util(self, model, tokenizer, prompt, max_length=256):
        inputs = tokenizer(prompt + self.custom_bos_token, return_tensors="pt", add_special_tokens=False)
        del inputs['token_type_ids']
        inputs = {k: v.to(model.device) for k, v in inputs.items()}
        output_ids = model.generate(**inputs, max_length=max_length,
                                    eos_token_id=tokenizer.eos_token_id)
        output = tokenizer.decode(output_ids[0], skip_special_tokens=False)
        return output_ids, output
    
    def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
        outputs = super().compute_loss(model, inputs, return_outputs=return_outputs, num_items_in_batch=num_items_in_batch)
        self._lossfreebalance(model)
        return outputs

    def training_step(self, model, inputs, num_items_in_batch):
        outputs = super().training_step(model, inputs, num_items_in_batch)
        _metrics = {}
        for name, param in model.named_parameters():
            if "router" in name and "weight" in name:
                # print(name, param.grad)
                if param.grad is None:
                    continue
                _metrics[name] = param.grad.abs().mean().item()
        if _metrics != {}:
            self.log(_metrics)
        return outputs

    def _lossfreebalance(self, model):
        if model.config.router_type in ['gate', 'random']:
            _metrics = {}
            if model._moe_router_counts[0] is not None:
                _metrics["choice_counts"] = model._moe_router_counts[0]
            if model._moe_router_counts[1] != 0:
                _metrics["aux_loss"] = model._moe_router_counts[1].item()
            print(_metrics)

            def calculate_entropy(sublist):
                counter = Counter(sublist)
                length = len(sublist)
                entropy = 0.0
                
                for count in counter.values():
                    probability = count / length
                    entropy -= probability * math.log2(probability)
                
                return entropy

            def safe_flatten(lst):
                result = []
                for item in lst:
                    if isinstance(item, (list, tuple)):
                        result.extend(safe_flatten(item))
                    else:
                        result.append(item)
                return result

            positions = []
            for i in range(len(_metrics["choice_counts"]['sample_0'])):
                position = []
                for sample in _metrics["choice_counts"].values():
                    position.extend(safe_flatten(sample[i]))
                positions.append(position)

            entropies = [calculate_entropy(position) for position in positions]
            entropy_metrics = {}
            for i, entropy in enumerate(entropies):
                entropy_metrics[f"router.{i}.entropy"] = entropy
            self.log(entropy_metrics)

            if model.config.router_type == 'gate':
                for idx_router in range(model.config.num_choices):
                    expert_counts = torch.bincount(model.topk_idxs[idx_router].flatten(), minlength=model.config.num_branches)
                    avg_count = sum(expert_counts).float()/len(expert_counts)
                    for i, count in enumerate(expert_counts):
                        error = avg_count - count.float()
                        model.router[idx_router].e_score_correction_bias.data[i] += model.config.update_rate * torch.sign(error)
                    print("e_score_correction_bias", model.router[idx_router].e_score_correction_bias.data)
        model.topk_idxs = []

    def _sample_distributed(self, samples, rank, world_size):
        sampler_rank = DistributedSampler(
            samples,
            num_replicas=world_size,
            rank=rank,
            shuffle=False,
            drop_last=True
        )        
        
        sampler_rank.set_epoch(0)
        indices_rank = list(sampler_rank)
        samples_rank = samples.select(indices_rank)
        num_samples_rank = len(indices_rank)
        print(f" [Rank {rank}] indices_rank: {indices_rank}, {samples_rank.to_dict()}")
        return samples, num_samples_rank        

    def print_trainable_parameters(self, model=None):
        """
        Prints the number of trainable parameters in the model.
        """
        if model is None:
            model = self.model

        trainable_params = 0
        all_param = 0
        for _, param in model.named_parameters():
            all_param += param.numel()
            if param.requires_grad:
                trainable_params += param.numel()
        print(
            f"raw model trainable params: {trainable_params} || all params: {all_param} || trainable%: {100 * trainable_params / all_param}"
        )