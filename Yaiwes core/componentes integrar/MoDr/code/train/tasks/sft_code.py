import os
import re
import yaml
import argparse

from dataclasses import dataclass, field, asdict

from transformers import PreTrainedTokenizerFast
from transformers import TrainingArguments, HfArgumentParser
from transformers.integrations.deepspeed import (
    unset_hf_deepspeed_config,
)
from peft import LoraConfig, TaskType, get_peft_model
from datasets import load_dataset
from transformers import set_seed
from swanlab.integration.transformers import SwanLabCallback

from train.raven_collator import CollatorForCompletionOnly
from train.raven_config_minimal import RavenConfig
from train.raven_trainer import RavenTrainer
from train.raven_modeling_minimal import RavenForCausalLM, svd_decompose

def formatting_prompt_func(example, tokenizer, custom_bos_token, label_type="answer"):
    messages = []
    messages.append({
        "role": "system",
        "content": "You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions."
    })
    messages.append({
        "role": "user", 
        "content": f"### Instruction:\n{example['problem']}\n\n### Response:"
    })
    if label_type == "answer":
        messages.append({
            "role": "Huginn", 
            "content": f"{example['answer']}"
        })
    elif label_type == "solution":
        messages.append({
            "role": "Huginn", 
            "content": f"{example['solution']}"
        }) 
    else:
        raise ValueError(f"Unknown label: {label_type}")
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    prompt = prompt.rsplit("<|begin_header|>Huginn<|end_header|>", 1)[0]

    return {"text": prompt}

def preprocess_dataset(dataset_path, tokenizer, max_seq_len, max_samples=100, custom_bos_token=None, label_type="answer"):
    raw_dataset = load_dataset("json", data_files={"train": dataset_path})["train"]
    if raw_dataset is not None and isinstance(max_samples, int) and max_samples < len(raw_dataset):
        raw_dataset = raw_dataset.select(range(max_samples))
    dataset = raw_dataset.map(lambda v: formatting_prompt_func(v, tokenizer, custom_bos_token, label_type), keep_in_memory=True)
    dataset = dataset.remove_columns([col for col in dataset.column_names if col != 'text'])

    # Print the first 5 formatted samples
    for i, sample in enumerate(dataset[:3]['text']):
        print(f"Sample {i + 1}:\n{sample}\n")

    raw_total = len(dataset)
    dataset = dataset.filter(lambda x: len(tokenizer(x['text'], add_special_tokens=False)['input_ids']) <= max_seq_len)
    filtered_proportion = len(dataset) / raw_total
    print(f"Proportion of samples with token length <= {max_seq_len}: {filtered_proportion:.2%}")

    return raw_dataset, dataset

def rename_last_checkpoint_to_final(folder_path):
    files = os.listdir(folder_path)
    
    checkpoint_files = [f for f in files if re.match(r'checkpoint-\d+', f)]
    
    if not checkpoint_files:
        print("Do not find checkpoint files.")
        return
    
    checkpoint_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))
    
    last_checkpoint = checkpoint_files[-1]
    
    old_path = os.path.join(folder_path, last_checkpoint)
    new_path = os.path.join(folder_path, 'final')
    
    try:
        os.rename(old_path, new_path)
        print(f" {last_checkpoint} renamed to final.")
    except Exception as e:
        print(f"Renaming failed: {e}")


@dataclass
class ModelArgs:
    model_path: str = field(
        default=None,
        metadata={"help": "Path to the pre-trained model."},
    )
    dataset_path: str = field(
        default=None,
        metadata={"help": "Path to the dataset used for training."},
    )
    max_seq_len: int = field(
        default=256,
        metadata={"help": "Maximum sequence length for input tokens."},
    )
    max_samples: int = field(
        default=None,
        metadata={"help": "Maximum number of samples to use from the dataset."},
    )
    router_type: str = field(
        default='gate',
        metadata={"help": "Type of router to use in the model."},
    )
    num_branches: int = field(
        default=3,
        metadata={"help": "Number of branches in the model."},
    )
    num_steps: str = field(
        default="3,3",
        metadata={"help": "Number of steps for each branch, specified as a comma-separated string."},
    )
    per_branch_depth: int = field(
        default=1,
        metadata={"help": "Depth of each branch in the model."},
    )
    mean_backprop_depth: int = field(
        default=1,
        metadata={"help": "Expected number of recurrences in the model."},
    )
    mean_recurrence: int = field(
        default=1,
        metadata={"help": "Mean depth for backpropagation through time."},
    )
    num_choices: int = field(
        default=3,
        metadata={"help": "Number of choices available in the model."},
    )
    use_peft: str = field(
        default=None,
        metadata={"help": "Whether to use Parameter-Efficient Fine-Tuning (PEFT) for training."},
    )
    custom_bos_token: str = field(
        default="<|begin_header|>Huginn<|end_header|>",
        metadata={"help": "Custom beginning of sequence token used in the model."},
    )
    label_type: str = field(
        default="answer",
        metadata={"help": "Label type. optional: answer or solution."},
    )
    topk_method: str = field(
        default="greedy",
        metadata={"help": "Method for top-k selection in branch routing."},
    )
    scoring_func: str = field(
        default="softmax",
        metadata={"help": "Scoring function for branch routing."},
    )
    aux_loss_alpha: float = field(
        default=0.01,
        metadata={"help": "Alpha for auxiliary loss in branch routing."},
    )
    update_rate: float = field(
        default=1e-4,
        metadata={"help": "Update rate for branch routing."},
    )
    lora_r: int = field(
        default=16,
        metadata={"help": "Rank of the LoRA matrix."},
    )
    lora_alpha: int = field(
        default=16,
        metadata={"help": "Alpha for the LoRA matrix."},
    )
    is_debug: bool = field(
        default=False,
        metadata={"help": "Whether to run in debug mode."},
    )
    swanlab_project: str = field(    
        default=None,
        metadata={"help": "SwanLab ID."},
    )

def print_dict_trainable_parameters(dict_params):
    vector_trainable_params = 0
    for k, v in dict_params.items():
        if v.requires_grad:
            vector_trainable_params += v.numel()
    print(f"dict_params: {vector_trainable_params}")


def merge_param_dict(param_dict, model, idx=0):
    for key, value in param_dict.items():
        if "__Wqkv__0__A" in key:
            key = key.replace("__Wqkv__0__A", f"__Wqkv__{idx}__A")
        elif "__Wqkv__0__B" in key:
            key = key.replace("__Wqkv__0__B", f"__Wqkv__{idx}__B")
        elif "__proj__0__A" in key:
            key = key.replace("__proj__0__A", f"__proj__{idx}__A")
        elif "__proj__0__B" in key:
            key = key.replace("__proj__0__B", f"__proj__{idx}__B")
        else:
            print("error key: ", key)
        for k, v in model.lora_decompose_param_dict.items():
            if key in k:
                model.lora_decompose_param_dict[k] = value
                model.lora_decompose_param_dict[k].requires_grad = True
                break
    return model


def main():
    parser = HfArgumentParser([TrainingArguments, ModelArgs])
    training_args, model_args, _ = parser.parse_args_into_dataclasses(return_remaining_strings=True)

    set_seed(training_args.seed)
    print(f"Seed: {training_args.seed}")

    model_path =  model_args.model_path
    dataset_path = model_args.dataset_path
    max_sequence_length = model_args.max_seq_len
    max_samples = model_args.max_samples
    num_branches = model_args.num_branches
    num_choices = model_args.num_choices
    mean_backprop_depth = model_args.mean_backprop_depth
    mean_recurrence = model_args.mean_recurrence
    per_branch_depth = model_args.per_branch_depth
    custom_bos_token = model_args.custom_bos_token
    label_type = model_args.label_type
    topk_method = model_args.topk_method
    scoring_func = model_args.scoring_func
    aux_loss_alpha = model_args.aux_loss_alpha
    update_rate = model_args.update_rate
    lora_r = model_args.lora_r
    lora_alpha = model_args.lora_alpha
    swanlab_project = model_args.swanlab_project
    print(f"Train args: {training_args}\n{model_args}")

    tokenizer = PreTrainedTokenizerFast.from_pretrained(model_path, trust_remote_code=True)
    raw_dataset, dataset = preprocess_dataset(dataset_path, tokenizer, max_sequence_length, max_samples, custom_bos_token, label_type)

    router_type = model_args.router_type
    if model_args.num_steps not in [None, 'None']:
        num_steps = model_args.num_steps.split(",")
        num_steps = (int(num_steps[0]), int(num_steps[1]))
    else:
        num_steps = None

    target_modules = [
        "transformer.core_block.0.attn.Wqkv",
        "transformer.core_block.0.attn.proj",
        "transformer.core_block.1.attn.Wqkv",
        "transformer.core_block.1.attn.proj",
        "transformer.core_block.2.attn.Wqkv",
        "transformer.core_block.2.attn.proj",
        "transformer.core_block.3.attn.Wqkv",
        "transformer.core_block.3.attn.proj",
    ]

    fine_tuning_algorithm = model_args.use_peft.lower() if model_args.use_peft is not None else None
    model_config = RavenConfig.from_pretrained(model_path)
    model_config.per_branch_depth = per_branch_depth
    model_config.router_type = router_type
    model_config.topk_method = topk_method
    model_config.scoring_func = scoring_func
    model_config.aux_loss_alpha = aux_loss_alpha
    model_config.update_rate = update_rate
    model_config.num_steps = num_steps
    model_config.num_branches = num_branches
    model_config.num_choices = num_choices
    model_config.mean_backprop_depth = mean_backprop_depth
    model_config.mean_recurrence = mean_recurrence
    model_config.fine_tuning_algorithm = fine_tuning_algorithm
    model_config.target_modules = target_modules
    model_config.lora_r = lora_r
    model_config.lora_alpha = lora_alpha
    model = RavenForCausalLM.from_pretrained(model_path, config=model_config, trust_remote_code=True)
    if training_args.deepspeed is not None:
        unset_hf_deepspeed_config()

    if model_args.use_peft.lower() == "lora_peft":
        lora_config = LoraConfig(
            task_type=TaskType.CAUSAL_LM,
            r=16,
            lora_alpha=16,
            target_modules=target_modules,
            bias="none"
        )
        model = get_peft_model(model, lora_config)

    elif model_args.use_peft.lower() == "svd":
        for name, param in model.named_parameters():
            if "singular_scale" not in name:
                param.requires_grad = False
        if model.svd_decompose_param_dict is None:
            model.svd_decompose_param_dict = svd_decompose(model, target_modules, model.config.svd_cache_file)
        model.apply_svd_hook()

    elif model_args.use_peft.lower() == "lora":
        for name, param in model.named_parameters():
            if not name.endswith("__A") and not name.endswith("__B"):
                param.requires_grad = False
        model.apply_lora_hook()

    if router_type != "gate":
        model.router = None
    else:
        try:
            for router in model.router:
                router.weight.requires_grad = True
                if router.topk_method == "noaux_tc":
                    router.e_score_correction_bias.requires_grad = True
        except:
            model.router.weight.requires_grad = True
            if model.router.topk_method == "noaux_tc":
                model.router.e_score_correction_bias.requires_grad = True

    model.reset_parameters()

    collator = CollatorForCompletionOnly(tokenizer=tokenizer,
                                         max_sequence_length=max_sequence_length,
                                         log_level=training_args.log_level,
                                         custom_bos_token=custom_bos_token)

    swanlab_callback = SwanLabCallback(
        project=swanlab_project,
        workspace="MoDr",
        experiment_name=training_args.output_dir.split("/")[-1]
    )

    trainer = RavenTrainer(
        model=model,
        train_dataset=dataset,
        eval_dataset=raw_dataset,
        args=training_args,
        data_collator=collator,
        custom_bos_token=custom_bos_token,
        callbacks=[swanlab_callback]
    )

    trainer.print_trainable_parameters()
    trainer.train()

    with open(os.path.join(training_args.output_dir, 'train_args.yaml'), 'w') as file:
        yaml.dump(training_args.to_dict(), file)
    with open(os.path.join(training_args.output_dir, 'model_args.yaml'), 'w') as file:
        yaml.dump(asdict(model_args), file)
    with open(os.path.join(training_args.output_dir, 'model_config.yaml'), 'w') as file:
        yaml.dump(model_config.to_dict(), file)

    rename_last_checkpoint_to_final(training_args.output_dir)


if __name__ == "__main__":
    main()
