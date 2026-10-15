import ray
import torch
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

@ray.remote
class InferenceActor:
    def __init__(self, model_name_or_path: str, device: str = "cuda"):
        self.device = device
        self.model = None
        self.tokenizer = None
        self.model_name_or_path = model_name_or_path
        
    def init_model(self):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name_or_path, 
            torch_dtype=torch.bfloat16, 
            trust_remote_code=True
        )
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)
        self.model.eval()
        self.model.to(self.device)
        
    def infer(self, inputs: List[str], **kwargs) -> List[Dict[str, Any]]:
        if self.model is None:
            self.init_model()
            
        results = []
        for input_text in inputs:
            input_ids = self.tokenizer(input_text, return_tensors="pt", add_special_tokens=True).to(self.device)
            del input_ids["token_type_ids"]
            
            outputs = self.model.generate(
                **input_ids,
                tokenizer=self.tokenizer,
                eos_token_id=self.tokenizer.eos_token_id,
                **kwargs
            )
            
            response = self.tokenizer.decode(outputs[0])
            results.append({
                "input": input_text,
                "output": response,
                "input_ids": input_ids,
                "output_ids": outputs
            })
            
        return results 