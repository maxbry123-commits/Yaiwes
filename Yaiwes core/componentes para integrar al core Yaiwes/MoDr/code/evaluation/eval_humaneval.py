import re
import ast
import json
import os
import tempfile
import subprocess
import argparse
import time
import datetime

from tqdm import tqdm
from datasets import load_dataset

import torch
from transformers import PreTrainedTokenizerFast, GenerationConfig
from train.raven_modeling_minimal import RavenForCausalLM, RavenConfig

from utils.utils import set_seed

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--origin_model_path', type=str, default=None, help="model dir")
    parser.add_argument('--checkpoint_path', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--end_idx', type=int, default=-1)
    parser.add_argument('--max_tokens', type=int, default=1024)
    parser.add_argument('--top_p', type=float, default=0.95)
    parser.add_argument('--num_steps', type=int, default=16)
    parser.add_argument('--num_choices', type=int, default=1)
    parser.add_argument("--temperature", default=0.0001, type=float)
    parser.add_argument("--original_huginn", type=bool, default=False)
    return parser.parse_args()

args = parse_args()

if not args.original_huginn:
    tokenizer = PreTrainedTokenizerFast.from_pretrained(args.origin_model_path)
    config = RavenConfig.from_pretrained(args.checkpoint_path)
    model = RavenForCausalLM.from_pretrained(args.checkpoint_path, config=config, torch_dtype=torch.float16)
    if "lora" == model.config.fine_tuning_algorithm:
        model.apply_lora_hook()
else:
    from transformers import AutoModelForCausalLM
    tokenizer = PreTrainedTokenizerFast.from_pretrained(args.origin_model_path)
    model = AutoModelForCausalLM.from_pretrained(args.origin_model_path, torch_dtype=torch.bfloat16, trust_remote_code=True)

model = model.to(dtype=torch.float16)
model = model.eval()
model = model.cuda()

if not args.original_huginn:
    model_name = "/".join(args.checkpoint_path.split("/")[-2:])
    model_name = model_name.replace("/", "_")
else:
    model_name = "original_huginn"

SYSTEM_PROMPT_TEMPLATE = """You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions."""

PROMPT_TEMPLATE = """### Instruction:
Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

Function signature:
{example}

### Response:"""

def generate_one_completion(prompt: str) -> str:
    messages = []
    messages.append({
    "role": "system",
    "content": SYSTEM_PROMPT_TEMPLATE
    })
    messages.append({
        "role": "user",
        "content": PROMPT_TEMPLATE.format(example=prompt)
    })
    chat_input = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    config = GenerationConfig(max_length=args.max_tokens, 
                            use_cache=False,
                            do_sample=True,
                            temperature=args.temperature,
                            top_p=args.top_p,
                            top_k=None,
                            min_p=None,
                            return_dict_in_generate=True,
                            eos_token_id=65505,
                            bos_token_id=65504,
                            pad_token_id=65509,
                            stop_strings=["<|end_text|>", "<|end_turn|>"]
                            )
    model.config.router_choice_idx = None
    input_ids = tokenizer.encode(chat_input, return_tensors="pt", add_special_tokens=False).to("cuda")
    response = model.generate(input_ids, config, num_steps=args.num_steps, tokenizer=tokenizer)
    generated_text = tokenizer.decode(response.sequences[0][input_ids.shape[1]:], skip_special_tokens=False)

    return generated_text


def extract_python_code_from_llm_response(llm_response: str, entry_point: str = None) -> str:
    """
    Extract Python code blocks from LLM response, optionally validating if it contains the specified entry function.
    
    Args:
        llm_response (str): Complete response text from LLM
        entry_point (str, optional): Expected function name to find in the code. If provided, will validate if the code contains this function definition.
        
    Returns:
        str: Extracted Python code, returns empty string if validation fails
    """
    # Match all code blocks (supports ```python and ``` formats)
    pattern = r"```(?:python)?\s*(.*?)```"
    matches = re.findall(pattern, llm_response, re.DOTALL)
    
    if not matches:
        response = llm_response.replace("<|end_turn|>", "")

        try:
            # Try to find the starting position of the code block
            start = response.find('def ')
            if start == -1:
                return None, "No function definition found in response"
            
            # Extract all content from def to the end of the string
            code = response[start:]
            
            # Add necessary import statements (if the original code has type hints)
            if 'List[' in code:
                code = 'from typing import List\n' + code
            if 'Tuple[' in code:
                code = 'from typing import Tuple\n' + code
            
            # Validate AST
            ast.parse(code)
            return code
            
        except Exception as e:
            print("[WARNING] No code block found in the response.")
            return ""
    
    # If there are multiple code blocks, try to find the one containing the target function
    python_code = ""
    if entry_point:
        # Build regex pattern for function definition
        func_pattern = rf"def\s+{re.escape(entry_point)}\s*\("
        
        for match in matches:
            code_block = match.strip()
            if re.search(func_pattern, code_block):
                python_code = code_block
                break
        
        if not python_code:
            print(f"[WARNING] No code block containing function '{entry_point}' found.")
            return ""
    else:
        # If no entry_point is specified, return the first code block
        python_code = matches[0].strip()
        print("[INFO] Using the first code block (no entry_point specified for validation).")
    
    return python_code


def extract_function_body_ast(code_string: str) -> str:
    """
    Extract function body content from string using AST parsing
    """
    try:
        tree = ast.parse(code_string)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Get the line range of the function body
                start_line = node.body[0].lineno - 1  # AST line numbers start from 1
                end_line = node.body[-1].end_lineno if hasattr(node.body[-1], 'end_lineno') else node.body[-1].lineno
                
                # Extract function body content
                lines = code_string.split('\n')
                function_body = '\n'.join(lines[start_line:end_line])
                return function_body
    except Exception as e:
        print(f"AST parsing error: {e}")
    
    return ""

def evaluate_humaneval_passat1(timeout=10) -> float:
    """
    Load HumanEval data using datasets.load_dataset and evaluate model Pass@1
    Args:
        timeout: int, timeout duration
    Returns:
        pass_at_1: float, pass rate
    """
    set_seed(args.seed)
    dt_string = datetime.datetime.now().strftime("%m-%d_%H-%M")
    # Load HumanEval dataset
    dataset = load_dataset("/mnt/share2/datasets/openai_humaneval", split="test")
    total = 0
    passed = 0

    results = []

    idx = 0
    if not args.original_huginn:
        print(f"Evaluating {args.checkpoint_path} on HumanEval")
    else:
        print(f"Evaluating {args.origin_model_path} on HumanEval")
    for example in tqdm(dataset):
        if args.end_idx != -1 and idx >= args.end_idx:
            break

        total += 1
        task_id = example.get("task_id", "unknown")
        prompt = example.get("prompt", "")
        test = example.get("test", "")
        entry_point = example.get("entry_point", "")

        if not all([prompt, test, entry_point]):
            print(f"[WARNING] Incomplete data in task {task_id}, skipping.")
            continue
        
        try:
            # ------------------------------
            # 1. Call LLM to get model-generated function body code
            # ------------------------------
            llm_response = generate_one_completion(prompt)
            print("--------------------------------LLM Response--------------------------------")
            print(llm_response)
            model_code = extract_python_code_from_llm_response(llm_response, entry_point)
            print("--------------------------------Model Code--------------------------------")
            print(model_code)
            function_body = extract_function_body_ast(model_code)
            print("--------------------------------Function Body--------------------------------")
            print(function_body)

            if not function_body:
                print(f"[WARNING] No valid Python code extracted for task {task_id}, skipping.")
                continue

            # ------------------------------
            # 2. Concatenate: prompt (without function body) + function_body (function body) + test_code
            # ------------------------------
            full_code = prompt + function_body + "\n" + test + "\n" + f"check({entry_point})"
            print("--------------------------------Full Code--------------------------------")
            print(full_code)

            # ------------------------------
            # 3. Write to temporary .py file
            # ------------------------------
            with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as temp:
                temp_filename = temp.name
                temp.write(full_code)

            # ------------------------------
            # 4. Execute code and determine if it passes (check if output contains "passed")
            # ------------------------------
            passed_flag = False
            try:
                result = subprocess.run(
                    ["python3", temp_filename],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                success = result.returncode == 0
                output = result.stdout
                err = result.stderr

                if success:
                    passed_flag = True
                else:
                    print(f"[DEBUG] Task {task_id} output: {output.strip()}")
                    print(f"[DEBUG] Task {task_id} error: {err.strip()}")
            except subprocess.TimeoutExpired as e:
                print(f"[TIMEOUT] Task {task_id} execution timed out after {timeout} seconds")
            except Exception as e:
                print(f"[ERROR] Task {task_id} execution failed: {e}")
            finally:
                # Clean up temporary file
                try:
                    os.unlink(temp_filename)
                except:
                    pass

            if passed_flag:
                passed += 1
                print(f"✅ [PASS] Task {task_id}")
            else:
                print(f"❌ [FAIL] Task {task_id}")
            idx += 1

            results.append({
                "task_id": task_id,
                "prompt": prompt,
                "function_body": function_body,
                "response": llm_response,
                "passed": passed_flag
            })
            print(f"--------------------------------")
        except Exception as e:
            print(f"Error in task {task_id}: {e}")
            continue

    pass_at_1 = passed / total if total > 0 else 0.0
    print(f"\n📮 Evaluated {total} tasks, {passed} passed, Pass@1 = {pass_at_1:.4f}")

    with open(f"{args.output_path}/{model_name}_humaneval_results_{dt_string}_num{args.end_idx}_topp{args.top_p}_temp{args.temperature}_step{args.num_steps}_pass@1_{pass_at_1:.4f}.json", "w") as f:
        json.dump(results, f, indent=2)

    return pass_at_1

if __name__ == "__main__":
    start_time = time.time()
    evaluate_humaneval_passat1(10)
    elapsed = round(time.time() - start_time)
    elapsed = str(datetime.timedelta(seconds=elapsed))
    print("Finished. Total elapsed time (h:m:s): {}".format(elapsed))
    print(f"\n\n\n\n\n")