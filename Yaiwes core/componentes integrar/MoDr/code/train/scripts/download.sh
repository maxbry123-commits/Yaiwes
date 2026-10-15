cd "$(dirname "$0")/../.."
ROOT_DIR=$(pwd)

hf download --repo-type model tomg-group-umd/huginn-0125 --local-dir $ROOT_DIR/llm_zoo/huginn-0125