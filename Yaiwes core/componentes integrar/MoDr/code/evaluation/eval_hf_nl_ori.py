import json
import torch
from transformers import PreTrainedTokenizerFast, GenerationConfig, AutoModelForCausalLM
import importlib.util
import os
import argparse
from datetime import datetime
from tqdm import tqdm
from utils.utils import set_seed
from utils.parser import *
from utils.data_loader import load_data
from utils.math_normalization import *
from utils.grader import *
import pickle
from math import comb

# envs.VLLM_HOST_IP="0.0.0.0" or "127.0.0.1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

script_dir = os.path.dirname(os.path.abspath(__file__))

def parse_list(arg):
    return arg.split(',')

def save_completions(completions, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(completions, file)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--origin_model_path', type=str, default=None, help="model dir")
    parser.add_argument("--k", type=int, default=1, help="Value of k for pass@k calculation")
    parser.add_argument("--data_dir", default=f"{script_dir}/data", type=str)
    parser.add_argument('--data_name', type=str, default="ARC-Challenge", help='identify how to extract answer')
    parser.add_argument("--split", default="test", type=str)
    parser.add_argument('--start_idx', type=int, default=0, help="data[start:end]")
    parser.add_argument('--end_idx', type=int, default=100, help="data[start:end], if -1, data[start:]")
    parser.add_argument("--temperature", default=0.0001, type=float)
    parser.add_argument("--max_tokens", default=512, type=int)
    parser.add_argument("--prompt_type", default="qwen-instruct", type=str)
    parser.add_argument("--prompt_file_path", default=f"{script_dir}/prompts", type=str)
    parser.add_argument("--surround_with_messages", action="store_true")
    parser.add_argument("--use_few_shot", action="store_true")
    parser.add_argument("--output_dir", default=f"{script_dir}/outputs", type=str)
    parser.add_argument('--stop', type=parse_list)
    parser.add_argument("--top_p", default=1, type=float)
    parser.add_argument("--seed", default=0, type=int)
    parser.add_argument("--dtype", default='auto', type=str)
    parser.add_argument("--svd_cache_file", default='./decompose_tensor.pt', type=str)
    parser.add_argument("--completions_save_dir", default=f"{script_dir}/completions", type=str)
    parser.add_argument("--num_steps", default=16, type=int)
    parser.add_argument("--router_choice_idx", default=None, type=str)
    args = parser.parse_args()
    
    args.top_p = 1 if args.temperature == 0 else args.top_p # top_p must be 1 when using greedy 
    print(f"current stop list: {args.stop}")
    return args

def get_conversation_prompt_by_messages(tokenizer, messages):
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    return text

def get_three_prompt(prompt_type, input, data_name, dataset=None):
    file_path = os.path.join(script_dir, "prompts", prompt_type, f"{data_name}.py")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    # 动态导入模块
    spec = importlib.util.spec_from_file_location("dynamic_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if input and hasattr(module, 'system_nl_with_input_prompt'):
        system_prompt = module.system_nl_with_input_prompt
    elif not input and hasattr(module, 'system_nl_without_input_prompt'):
        system_prompt = module.system_nl_without_input_prompt
    else:
        raise AttributeError(f"'system_nl_with_input_prompt' or 'system_nl_without_input_prompt' not found in {file_path}")
    
    if hasattr(module, 'few_shot_prompt'):
        few_shot_prompt = module.few_shot_prompt
    else:
        raise AttributeError(f"'few_shot_prompt' not found in {file_path}")
    
    if dataset in ["gpqa", "super-gpqa"]:
        if hasattr(module, 'gpqa_few_shot_prompt'):
            few_shot_prompt = module.gpqa_few_shot_prompt
        else:
            raise AttributeError(f"'gpqa_few_shot_prompt' not found in {file_path}")
    
    if input and hasattr(module, 'question_format_with_input'):
        question_format = module.question_format_with_input
    elif not input and hasattr(module, 'question_format_without_input'):
        question_format = module.question_format_without_input
    else:
        raise AttributeError(f"'question_format_with_input' or 'question_format_without_input' not found in {file_path}")

    return system_prompt, few_shot_prompt, question_format

def extract_huginn_answer(text):
    pattern = r'<\|begin_header\|>Huginn<\|end_header\|>(.*?)<\|end_turn\|>'
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    return ""

def extract_answer_from_response(response):
    pattern = r'(Answer\d+):'
    match = re.search(pattern, response, re.IGNORECASE)
    
    if match:
        return match.group(1).lower()
    else:
        return ""


def infer(args):
    model_name_or_path = args.origin_model_path
    print(f"current eval model: {model_name_or_path}")
        
    examples = load_data(args.data_name, args.split, args.data_dir, type="nl")
    if args.end_idx == -1:
        args.end_idx = len(examples)
    examples = examples[args.start_idx:args.end_idx]
    
    dt_string = datetime.now().strftime("%m-%d_%H-%M")
    model_name = "/".join(model_name_or_path.split("/")[-1:])
    model_name = model_name.replace("/", "_")
    out_file_prefix = f'{args.split}_t{args.temperature}_dt{dt_string}'
    if args.router_choice_idx is not None:
        out_file = f'{args.output_dir}/{model_name}/{args.data_name}/{out_file_prefix}_stp{args.num_steps}_s{args.start_idx}_e{args.end_idx}_rc{args.router_choice_idx}.jsonl'
    else:
        out_file = f'{args.output_dir}/{model_name}/{args.data_name}/{out_file_prefix}_stp{args.num_steps}_s{args.start_idx}_e{args.end_idx}.jsonl'
    generate_output_file = f'{args.output_dir}/{model_name}/{args.data_name}/{out_file_prefix}_stp{args.num_steps}_s{args.start_idx}_e{args.end_idx}_generation.json'

    if os.path.exists(out_file):
        print(f"Completely same name file({out_file}) exist, skip generation, save file and check correct")
        return
    os.makedirs(f'{args.output_dir}/{model_name}/{args.data_name}', exist_ok=True)
    available_gpus = os.environ.get('CUDA_VISIBLE_DEVICES', '0').split(',')
    print(f"available_gpus: {available_gpus}")
    tokenizer = PreTrainedTokenizerFast.from_pretrained(args.origin_model_path)
    prompt_batch = []
    for example in tqdm(examples, total=len(examples)):
        # parse question and answer
        if "input" in example and example["input"]:
            instruction = example["instruction"]
            input = example["input"]
        else:
            instruction = example["instruction"]
            input = ""
        system_prompt, few_shot_prompt, question_format = get_three_prompt(args.prompt_type, input, "general", args.data_name)
        
        if args.use_few_shot:
            if input:   
                cur_prompt = few_shot_prompt + question_format.format(instruction=instruction, input=input)
            else:
                cur_prompt = few_shot_prompt + question_format.format(instruction=instruction)
        else:
            if input:
                cur_prompt = question_format.format(instruction=instruction, input=input)
            else:
                cur_prompt = question_format.format(instruction=instruction)
        if True:# if args.surround_with_messages:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": cur_prompt}
            ]
            cur_prompt = get_conversation_prompt_by_messages(tokenizer=tokenizer, messages=messages)
        prompt_batch.append(cur_prompt)
    print(prompt_batch[0])
    
    llm = AutoModelForCausalLM.from_pretrained(args.origin_model_path, torch_dtype=torch.bfloat16, trust_remote_code=True)
    llm = llm.eval()
    llm = llm.cuda()

    config = GenerationConfig(
        max_length=args.max_tokens, 
        temperature=args.temperature,
        top_p=args.top_p,
        stop_strings=["<|end_text|>", "<|end_turn|>"], 
        use_cache=True,
        do_sample=True, 
        top_k=None,
        min_p=None,
        return_dict_in_generate=True,
        eos_token_id=65505,
        bos_token_id=65504,
        pad_token_id=65509)
    
    file_outputs = []
    correct_cnt = 0
    for i, data in enumerate(tqdm(prompt_batch)):
        try:
            input_ids = tokenizer.encode(data, return_tensors="pt", add_special_tokens=False).to("cuda")
            outputs = llm.generate(input_ids, config, tokenizer=tokenizer, num_steps=args.num_steps)
            response = tokenizer.decode(outputs.sequences[0], skip_special_tokens=False)
            response = extract_huginn_answer(response)
        except Exception as e:
            print(f"Error generating response: {e}")
            response = ""
        d = examples[i]
        question = d["instruction"]
        generated_responses = []
        generated_responses.append(response)
        file_outputs.append({
            "question": question,
            "generated_responses": generated_responses,
        })
        if "id" in d:
            file_outputs[i]["id"] = d["id"]
        if "source" in d:
            file_outputs[i]["source"] = d["source"]
    print(f"llm generate done, count: {len(file_outputs)}")

    pass_at_k_list = []
    k = args.k
    
    for i in tqdm(range(len(examples)), "check correct..."):
        d = examples[i]
        gt_cot, gt_ans = parse_ground_truth(d, args.data_name)
        generated_responses = file_outputs[i]['generated_responses']
        generated_answers = [extract_answer_from_response(generated_response) for generated_response in generated_responses]
        is_correct_list = [check_is_correct(generated_answer, gt_ans) for generated_answer in generated_answers]
        is_correct = any(is_correct_list)
        if is_correct:
            correct_cnt += 1
        file_outputs[i]['generated_answers'] = generated_answers
        file_outputs[i]['gold_answer'] = gt_ans
        file_outputs[i]['is_correct'] = is_correct
        file_outputs[i]['answers_correctness'] = is_correct_list
        
        if len(is_correct_list) > 1:
            correct_answers = sum(is_correct_list)
            n = len(generated_answers)
            if correct_answers > 0:
                if n - correct_answers < k:
                    pass_at_k = 1
                else:
                    pass_at_k = 1 - (comb(n - correct_answers, k) / comb(n, k))
                pass_at_k_list.append(pass_at_k)
            else:
                pass_at_k_list.append(0)
                
    temp_out_file = out_file + ".tmp"
    with open(temp_out_file, 'w', encoding='utf-8') as f:
        count = 0
        for d in tqdm(file_outputs, "writing generation to jsonl file..."):
            f.write(json.dumps(d, ensure_ascii=False))
            f.write("\n")
            count += 1
            if count % 100 == 0:
                f.flush()
        f.flush()
    os.rename(temp_out_file, out_file)
    
    output_content = []
    output_content.append(f"correct cnt / total cnt: {correct_cnt}/{len(examples)}")
    output_content.append(f"Acc: {correct_cnt / len(examples):.4f}")
    print(f"correct cnt / total cnt: {correct_cnt}/{len(examples)}")
    print(f"Acc: {correct_cnt / len(examples):.4f}")

    if pass_at_k_list:
        average_pass_at_k = sum(pass_at_k_list) / len(pass_at_k_list)
        output_content.append(f"Pass@{k}: {sum(pass_at_k_list)}/{len(pass_at_k_list)} = {average_pass_at_k:.4f}")
        print(f"Pass@{k}: {sum(pass_at_k_list)}/{len(pass_at_k_list)} = {average_pass_at_k:.4f}")
    else:
        output_content.append(f"Pass@1: {correct_cnt}/{len(examples)} = {correct_cnt / len(examples):.4f}")
        print(f"Pass@1: {correct_cnt}/{len(examples)} = {correct_cnt / len(examples):.4f}")

    acc = f"{correct_cnt / len(examples):.4f}"
    os.rename(out_file, out_file.replace(".jsonl", f"_pass@1-{acc}.jsonl"))


if __name__ == "__main__":
    args = parse_args()
    set_seed(args.seed)
    infer(args)
