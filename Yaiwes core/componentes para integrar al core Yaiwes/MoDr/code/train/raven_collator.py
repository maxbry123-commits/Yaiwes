import numpy as np
import torch


def fixed_decode(token_ids, tokenizer):
    outputs = []
    for tid in token_ids:
        if tid != -100:
            token = tokenizer.convert_ids_to_tokens(tid.tolist())
            token = token.replace('Ġ', ' ').replace('Ċ', '\n')
            outputs.append(token)
        else:
            outputs.append("<-100>")
    return "".join(outputs)


class CollatorForCompletionOnly:

    def __init__(self, tokenizer, max_sequence_length, log_level, custom_bos_token):
        self.tokenizer = tokenizer
        self.max_sequence_length = max_sequence_length
        self.log_level = log_level
        self.custom_bos_token = custom_bos_token

    def __call__(self, features):
        batch_labels = []
        batch_input_ids = []
        batch_attention_mask = []

        custom_bos_token_ids = torch.tensor(self.tokenizer.encode(self.custom_bos_token, add_special_tokens=False))

        for i, example in enumerate(features):
            inputs = self.tokenizer(example['text'], max_length= self.max_sequence_length, padding='max_length', add_special_tokens=False, return_tensors="pt")
            input_ids = inputs['input_ids'].reshape(-1)
            attention_mask = inputs['attention_mask'].reshape(-1)
            label = input_ids.clone()
            label[label == self.tokenizer.pad_token_id] = -100 #  ignore pad token

            bos_inxes = np.where(input_ids == custom_bos_token_ids[0])[0]
            matched = False
            for bos_inx in bos_inxes:
                if torch.equal(input_ids[bos_inx: bos_inx + len(custom_bos_token_ids)], custom_bos_token_ids):
                    matched = True
                    label[: bos_inx + len(custom_bos_token_ids)] = -100  # ignore source sequences
                    batch_input_ids.append(input_ids)
                    batch_labels.append(label)
                    batch_attention_mask.append(attention_mask)
                    break

            if not matched:
                raise RuntimeError(f"ERROR: example skipped since no bos found {example}")

        if self.log_level.upper() == 'DEBUG':
            print("collator_for_completion_only|begin")
            print("first decoded input_ids:", self.tokenizer.decode(batch_input_ids[0], skip_special_tokens=False))
            print("first label_ids:",  batch_labels[0])
            print("first decoded label_ids:", fixed_decode(batch_labels[0], self.tokenizer))
            print("first attention_mask:", batch_attention_mask[0])
            print("collator_for_completion_only|end")

        batch_input_ids = torch.stack(batch_input_ids)
        batch_attention_mask = torch.stack(batch_attention_mask)
        batch_labels = torch.stack(batch_labels)

        batch = {
            "input_ids": batch_input_ids,
            "attention_mask": batch_attention_mask,
            "labels": batch_labels
        }
        return batch