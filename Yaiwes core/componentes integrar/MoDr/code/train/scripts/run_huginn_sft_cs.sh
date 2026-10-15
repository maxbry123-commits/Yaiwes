cd "$(dirname "$0")/../.."
ROOT_DIR=$(pwd)

model_path=$ROOT_DIR/llm_zoo/huginn-0125
output_dir=$ROOT_DIR/checkpoints/huginn_sft_cs_$(date +%Y%m%d_%H%M%S)
eval_dir=$ROOT_DIR/results
dataset_path=$ROOT_DIR/datasets/commonsense_170k

echo "--------------------------------"
echo "Running Huginn SFT commonsense"
echo "--------------------------------"
echo "Model path: $model_path"
echo "Output directory: $output_dir"
echo "Dataset path: $dataset_path"
echo "--------------------------------"


CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python train/tasks/sft_cs.py \
    --model_path $model_path \
    --dataset_path $dataset_path \
    --output_dir $output_dir \
    --custom_bos_token "<|begin_header|>Huginn<|end_header|>" \
    --label_type answer \
    --per_device_train_batch_size 8 \
    --gradient_accumulation_steps 1 \
    --num_train_epochs 1 \
    --max_seq_len 256 \
    --max_samples 175000 \
    --learning_rate 4e-5 \
    --lr_scheduler_type cosine \
    --warmup_ratio 0.1 \
    --label_names labels \
    --router_type normal \
    --use_peft lora \
    --num_choices 1 \
    --num_branches 4 \
    --num_steps 16,4 \
    --mean_recurrence 32 \
    --mean_backprop_depth 8 \
    --topk_method noaux_tc \
    --scoring_func sigmoid \
    --num_branches_per_tok 1 \
    --aux_loss_alpha 0.000 \
    --update_rate 0.001 \
    --remove_unused_columns False \
    --save_steps 500 \
    --save_total_limit 1 \
    --do_eval False \
    --eval_strategy no \
    --eval_steps 100 \
    --log-level info \
    --logging_strategy steps \
    --logging_steps 1 \
    --seed 42 \
    --is_debug False \
    --run_name $output_dir \
    --report_to "none" \
    --max_grad_norm 0.2 \
    --weight_decay 1e-4 \
    --swanlab_project "Huginn-SFT-Commonsense" \


# Evaluation
mkdir -p $eval_dir


echo "--------------------------------"
echo "Huginn SFT piqa"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf_nl.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "piqa" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --surround_with_messages \

echo "--------------------------------"
echo "Huginn SFT hellaswag"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf_nl.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "hellaswag" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --surround_with_messages \

echo "--------------------------------"
echo "Huginn SFT winogrande"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf_nl.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "winogrande" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --surround_with_messages \

echo "--------------------------------"
echo "Huginn SFT ARC-Easy"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf_nl.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "ARC-Easy" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --surround_with_messages \

echo "--------------------------------"
echo "Huginn SFT ARC-Challenge"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf_nl.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "ARC-Challenge" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --surround_with_messages \

echo "--------------------------------"
echo "Huginn SFT openbookqa"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf_nl.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "openbookqa" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --surround_with_messages \
