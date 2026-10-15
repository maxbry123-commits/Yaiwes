import json
from transformers import AutoTokenizer
import importlib.util
import os
import time
import argparse
from datetime import datetime
from tqdm import tqdm
from utils.utils import set_seed
from utils.parser import *
from utils.data_loader import load_data
from utils.math_normalization import *
from utils.grader import *
from utils.call_llm_api import get_gpt_completion
import pickle
from math import comb
import logging
import typing

LOG_FORMAT = ("[%(asctime)s][%(filename)s - line %(lineno)s] "
              "- %(levelname)s - %(message)s")

logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


os.environ["TOKENIZERS_PARALLELISM"] = "false"

script_dir = os.path.dirname(os.path.abspath(__file__))

def parse_list(arg):
    return arg.split(',')

def save_completions(completions, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(completions, file)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name_or_path', type=str, default=f"/home/zhangxj/llm_zoo/huginn-0125", help="model dir")
    parser.add_argument("--k", type=int, default=1, help="Value of k for pass@k calculation")
    parser.add_argument("--data_dir", default=f"{script_dir}/data", type=str)
    parser.add_argument('--data_name', type=str, default="gsm8k", help='identify how to extract answer')
    parser.add_argument("--split", default="test", type=str)
    parser.add_argument('--start_idx', type=int, default=0, help="data[start:end]")
    parser.add_argument('--end_idx', type=int, default=3, help="data[start:end], if -1, data[start:]")
    parser.add_argument("--temperature", default=0.01, type=float)
    parser.add_argument("--max_tokens", default=2048, type=int)
    parser.add_argument("--prompt_type", default="qwen-instruct", type=str)
    parser.add_argument("--prompt_file_path", default=f"{script_dir}/prompts", type=str)
    parser.add_argument("--surround_with_messages", action="store_true")
    parser.add_argument("--use_few_shot", action="store_true")
    parser.add_argument("--output_dir", default=f"{script_dir}/outputs", type=str)
    parser.add_argument('--stop', type=parse_list)
    parser.add_argument("--top_p", default=1, type=float)
    parser.add_argument("--seed", default=0, type=int)
    parser.add_argument("--dtype", default='auto', type=str)
    parser.add_argument("--completions_save_dir", default=f"{script_dir}/completions", type=str)
    # parser.add_argument("--use_qwen_check", action="store_true")
    parser.add_argument("--num_steps", default=16, type=int)
    parser.add_argument('--batch-size', default=10, help='the number of chunk samples')
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

def get_three_prompt(prompt_type, data_name):
    file_path = os.path.join(script_dir, "prompts", prompt_type, f"{data_name}.py")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    # 动态导入模块
    spec = importlib.util.spec_from_file_location("dynamic_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if hasattr(module, 'system_prompt'):
        system_prompt = module.system_prompt
    else:
        raise AttributeError(f"'system_prompt' not found in {file_path}")
    
    if hasattr(module, 'few_shot_prompt'):
        few_shot_prompt = module.few_shot_prompt
    else:
        raise AttributeError(f"'few_shot_prompt' not found in {file_path}")
    
    if hasattr(module, 'question_format'):
        question_format = module.question_format
    else:
        raise AttributeError(f"'question_format' not found in {file_path}")

    return system_prompt, few_shot_prompt, question_format

class GeneratorAction:

    def __init__(self, 
                 llm_name: str='llama3',
                 temperature: float=0.6,
                 max_tokens: int=2048):
        self.llm_name = llm_name
        self.temperature = temperature
        self.max_tokens = max_tokens

        self.tokens_usages = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    
    def __call__(self, *args, **inputs: typing.Any):
        output = self._call(inputs)
        return output

    def _call(self, inputs: typing.Dict[str, typing.Any]):
        samples = inputs['samples']
        assert isinstance(samples, list), f'"samples" must be list'
        indices = inputs.get('indices', None) or range(len(samples))

        responses = []
        for idx in indices:
            try:
                pass
                prompt_sample = samples[idx]

                response_content, usage_tokens = get_gpt_completion(
                    prompt=prompt_sample,
                    model=self.llm_name, 
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,  
                    count_tokens=True)
                self.tokens_usages["prompt_tokens"] += usage_tokens[0]
                self.tokens_usages["completion_tokens"] += usage_tokens[1]
                self.tokens_usages["total_tokens"] += usage_tokens[2]

                responses.append(response_content)
            except KeyboardInterrupt:
                break
            except:
                import traceback
                traceback.print_exc()
                pass
        
        return responses


class Generator:

    def __init__(self, 
                 name: str,
                 llm_name: str='llama3',
                 temperature: float=0.6,
                 max_tokens: int=2048,
                 verbose: bool=False):
        self.name = name
        self.llm_name = llm_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.verbose = verbose

        self.time_cost = 0

    def handle(self, prompt_batch: list, tag: str):
        logger.info(f'handle batch for {tag}, prompt_batch_len={len(prompt_batch)}')

        start_time = time.time()

        generator = GeneratorAction(
            llm_name=self.llm_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        indices = range(len(prompt_batch))
        if self.verbose and len(prompt_batch) > 1:
            indices = tqdm(indices, desc='generate', leave=True)
        out = generator(samples=prompt_batch, indices=indices)
        assert isinstance(out, list)
        usage = generator.tokens_usages

        end_time = time.time()
        self.time_cost = end_time - start_time
        logger.info(f'finished in {self.time_cost:.3f} seconds. usages: {usage}')

        return out, usage, tag
    
    def __repr__(self):
        return f'{type(self).__name__}({self.name})'


def wait_ray_pool(ray_pool, fn_result):
    while not ray_pool.has_free():
        try:
            r = ray_pool.get_next_unordered(timeout=0.0)
            fn_result(r)
        except TimeoutError:
            time.sleep(0.3)

def main():
    model_name_or_path = args.model_name_or_path
    print(f"current eval model: {model_name_or_path}")
        
    examples = load_data(args.data_name, args.split, args.data_dir)
    if args.end_idx == -1:
        args.end_idx = len(examples)
    examples = examples[args.start_idx:args.end_idx]
    
    dt_string = datetime.now().strftime("%m-%d_%H-%M")
    model_name = "/".join(args.model_name_or_path.split("/")[-1:])
    out_file_prefix = f'{args.split}_{args.prompt_type}_t{args.temperature}_dt{dt_string}'
    out_file = f'{args.output_dir}/{model_name}/{args.data_name}/{out_file_prefix}_k{args.n_sampling}_s{args.start_idx}_e{args.end_idx}.jsonl'
    
    if os.path.exists(out_file):
        print(f"Completely same name file({out_file}) exist, skip generation, save file and check correct")
        return
    os.makedirs(f'{args.output_dir}/{model_name}/{args.data_name}', exist_ok=True)
    os.makedirs(f'{args.completions_save_dir}/{model_name}/{args.data_name}', exist_ok=True)
    
    # available_gpus = os.environ['CUDA_VISIBLE_DEVICES'].split(',')
    available_gpus = os.environ.get('CUDA_VISIBLE_DEVICES', '0').split(',')
    print(f"available_gpus: {available_gpus}")
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True)
    
    prompt_batches = []
    for example in tqdm(examples, total=len(examples)):
        # parse question and answer
        question = parse_question(example, args.data_name)
        system_prompt, few_shot_prompt, question_format = get_three_prompt(args.prompt_type, args.data_name)
        
        if args.use_few_shot:
            cur_prompt = few_shot_prompt + question_format.format(question=question)
        else:
            cur_prompt = question_format.format(question=question)
        if args.surround_with_messages:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": cur_prompt}
            ]
            cur_prompt = get_conversation_prompt_by_messages(tokenizer=tokenizer, messages=messages)
        prompt_batches.append(cur_prompt)

    use_ray = args.n_worker > 1

    ge_options = dict(
        llm_name=args.model_name_or_path,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        verbose=args.verbose and not use_ray,
    )

    if use_ray:
        import ray
        from ray.util.actor_pool import ActorPool
        rc = ray.init()
        logger.info(f'initialize ray: {rc}')
        remote_polisher = ray.remote(Generator)
        actors = [remote_polisher.remote(name=f'worker-{i}', **ge_options) for i in range(args.n_worker)]
        ge_pool = ActorPool(actors)
    else:
        ge = Generator(name='Generator', **ge_options)

    n_total = 0
    u_total = ModelUsage.zero()
    start_time = time.time()
    response_outputs = []

    def split_batch(prompt_batches: list, batch_size: int):
        for i in range(0, len(prompt_batches), batch_size):
            prompt_batch = prompt_batches[i: i + batch_size]
            yield prompt_batch

    def process_result(responses: list, usage_: ModelUsage, tag: str):
        response_outputs.extend(responses)

        n_total += len(responses)
        u_total += usage_
        now = time.time()
        elapsed = int(now - start_time)
        elapsed = int(now - start_time)
        if elapsed > 0 and n_total > 0:
            speed = n_total / elapsed
            if speed > 1:
                speed = f'{speed:.3f} sample/second'
            else:
                speed = f'{1 / speed:.3f}s/sample'
            speed += f', {u_total.completion_tokens // elapsed:,d} tokens/s'
        else:
            speed = '<na>'
        logger.info(f'got {tag}, total: {n_total} samples/{elapsed:,d} seconds. speed: {speed}')

        return True

    for i, prompt_batch in enumerate(
        split_batch(prompt_batches, args.batch_size)
    ):
        logger.info(f'>>> batch {i}, the number of batch is {len(prompt_batch)}')

        if use_ray:
            wait_ray_pool(ge_pool, fn_result=lambda r: process_result(r[0], r[1], r[2]))
            ge_pool.submit(lambda a, v: a.handle.remote(*v), (prompt_batch, f'batch-{i}'))
        else:
            out, usage, tag = ge.handle(prompt_batch, f'batch-{i}')
            process_result(out, usage, tag)

    pass_at_k_list = []
    correct_cnt = 0
    for i in tqdm(range(len(examples)), "check correct..."):
        d = examples[i]
        gt_cot, gt_ans = parse_ground_truth(d, args.data_name)
        generated_responses = response_outputs[i]['generated_responses']
        generated_answers = [extract_answer(generated_response, args.data_name) for generated_response in generated_responses]
        is_correct_list = [check_is_correct(generated_answer, gt_ans) for generated_answer in generated_answers]
        is_correct = any(is_correct_list)
        if is_correct:
            correct_cnt += 1
        response_outputs[i]['generated_answers'] = generated_answers
        response_outputs[i]['gold_answer'] = gt_ans
        response_outputs[i]['is_correct'] = is_correct
        response_outputs[i]['answers_correctness'] = is_correct_list
        
        if len(is_correct_list) > 1:
            correct_answers = sum(is_correct_list)
            n = len(generated_answers)
            if correct_answers > 0:
                if n - correct_answers < args.k:
                    pass_at_k = 1
                else:
                    pass_at_k = 1 - (comb(n - correct_answers, args.k) / comb(n, args.k))
                pass_at_k_list.append(pass_at_k)
            else:
                pass_at_k_list.append(0)
                
    temp_out_file = out_file + ".tmp"
    with open(temp_out_file, 'w', encoding='utf-8') as f:
        count = 0
        for d in tqdm(response_outputs, "writing generation to jsonl file..."):
            f.write(json.dumps(d, ensure_ascii=False))
            f.write("\n")
            count += 1
            if count % 100 == 0:
                f.flush()
        f.flush()
    os.rename(temp_out_file, out_file)
    
    print(f"correct cnt / total cnt: {correct_cnt}/{len(examples)}")
    print(f"Acc: {correct_cnt / len(examples):.4f}")

    if pass_at_k_list:
        average_pass_at_k = sum(pass_at_k_list) / len(pass_at_k_list)
        print(f"Pass@{args.k}: {sum(pass_at_k_list)}/{len(pass_at_k_list)} = {average_pass_at_k:.4f}")
    else:
        print(f"Pass@1: {correct_cnt}/{len(examples)} = {correct_cnt / len(examples):.4f}")

    end_time = time.time()

    logger.info('done')
    logger.info(f'{u_total.__repr__}')
    logger.info(f"Time cost: {end_time-start_time:.2f}s")
    return 0


if __name__ == "__main__":
    args = parse_args()
    set_seed(args.seed)
    main(args)
