cd "$(dirname "$0")/../.."
ROOT_DIR=$(pwd)

model_path=$ROOT_DIR/llm_zoo/huginn-0125
output_dir=$ROOT_DIR/checkpoints/modr_code_$(date +%Y%m%d_%H%M%S)
eval_dir=$ROOT_DIR/results
dataset_path=$ROOT_DIR/datasets/codefeedback_python_79k.json

echo "--------------------------------"
echo "Running MoDr code"
echo "--------------------------------"
echo "Model path: $model_path"
echo "Output directory: $output_dir"
echo "Dataset path: $dataset_path"
echo "--------------------------------"


CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python train/tasks/sft_code.py \
    --model_path $model_path \
    --dataset_path $dataset_path \
    --output_dir $output_dir \
    --custom_bos_token "<|begin_header|>Huginn<|end_header|>" \
    --label_type solution \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 1 \
    --num_train_epochs 4 \
    --max_seq_len 512 \
    --max_samples 100000 \
    --learning_rate 4e-5 \
    --lr_scheduler_type cosine \
    --warmup_ratio 0.1 \
    --label_names labels \
    --router_type gate \
    --use_peft lora \
    --num_choices 1 \
    --num_branches 4 \
    --num_steps 16,4 \
    --mean_recurrence 32 \
    --mean_backprop_depth 8 \
    --topk_method noaux_tc \
    --scoring_func sigmoid \
    --num_branches_per_tok 2 \
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
    --swanlab_project "MoDr-Code" \


echo "--------------------------------"
echo "MoDr humaneval"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_humaneval.py \
    --origin_model_path $model_path \
    --checkpoint_path $output_dir/final \
    --output_path $eval_dir \
    --seed 0 \
    --end_idx -1 \
    --max_tokens 1024 \
    --top_p 0.95 \
    --num_steps 16 \

echo "--------------------------------"
echo "MoDr mbpp"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_mbpp.py \
    --origin_model_path $model_path \
    --checkpoint_path $output_dir/final \
    --output_path $eval_dir \
    --seed 0 \
    --end_idx -1 \
    --max_tokens 1024 \
    --top_p 0.95 \
    --num_steps 16 \