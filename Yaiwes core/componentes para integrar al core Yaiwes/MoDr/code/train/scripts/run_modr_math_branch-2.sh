cd "$(dirname "$0")/../.."
ROOT_DIR=$(pwd)

model_path=$ROOT_DIR/llm_zoo/huginn-0125
output_dir=$ROOT_DIR/checkpoints/modr_math_$(date +%Y%m%d_%H%M%S)
eval_dir=$ROOT_DIR/results

echo "--------------------------------"
echo "Branch-2 gsm8k"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "gsm8k" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --router_choice_idx "2" \
    --surround_with_messages \

echo "--------------------------------"
echo "Branch-2 multiarith"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "multiarith" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --router_choice_idx "2" \
    --surround_with_messages \

echo "--------------------------------"
echo "Branch-2 addsub"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "addsub" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --router_choice_idx "2" \
    --surround_with_messages \


echo "--------------------------------"
echo "Branch-2 singleeq"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "singleeq" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --router_choice_idx "2" \
    --surround_with_messages \

echo "--------------------------------"
echo "Branch-2 aqua"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "aqua" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --router_choice_idx "2" \
    --surround_with_messages \

echo "--------------------------------"
echo "Branch-2 mawps"
echo "--------------------------------"
CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. python evaluation/eval_hf.py \
    --model_name_or_path $output_dir/final \
    --origin_model_path $model_path \
    --output_dir $eval_dir \
    --data_name "mawps" \
    --temperature 0.0001 \
    --start_idx 0 \
    --end_idx -1 \
    --split "test" \
    --max_tokens 1024 \
    --top_p 0.95 \
    --seed 0 \
    --num_steps 16 \
    --num_choices 1 \
    --router_choice_idx "2" \
    --surround_with_messages \