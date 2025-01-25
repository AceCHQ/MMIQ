# Evaluation Guidelines
We provide detailed instructions for evaluation. 
To execute our evaluation script, please ensure that the structure of your model outputs is the same as ours.

We provide two options:
1. Evaluation only: you can parse the response on your own and simply provide one file with all the final predictions.
2. Parse and evaluation: you can leave all the responses to us with the output formats shown below.

## Evaluation Only
If you want to use your own parsing logic and *only provide the final answer*, you can use `main_eval_only.py`.

You can provide all the outputs in *one file* in the following format:

```
{
    "data_id": "0",
    "categoty": "Temporal Movement",
    "parsed_pred": "A" 
},

{
    "data_id": "1",
    "categoty": "Temporal Movement",
    "parsed_pred": "D"
},

```


Then run eval_only with:
```
python main_eval_only.py --output_path ./example_outputs/exampple_output_parsed.jsonl --input_path ./MMIQ_benchmark_answer_dict.jsonl
```

Please refer to [example output](https://github.com/AceCHQ/MMIQ/blob/main/mmiq/example_outputs/output_example.jsonl) for a detailed prediction file form.


## Parse and Evaluation
You can also provide response and run the `main_parse_and_eval.py` to use our answer parsing processing and evaluation pipeline as follows:

### Output file
Each `output.jsonl`` has lines of json, each containing an instance for evaluation ().
```
    {
        "data_id": "0",
        "categoty": "Temporal Movement",
        "response": "The most appropriate option to fill in the question mark is option A." # model response
    },

    {
        "data_id": "1",
        "categoty": "Temporal Movement",
        "response": "The most appropriate option is D" # model response
    },
    ...
```

### Evaluation
```
python main_parse_and_eval.py --output_path ./example_outputs/example_model_output/output_example.jsonl --input_path ./MMIQ_benchmark_answer_dict.jsonl            
```

`main_parse_and_eval.py` will generate `result.json` under the same folder with `output_path`.

```
├── Model1
│   ├── output.json
│   └── result.json
└── Model2
    ├── output.json
    └── result.json
...
```

## Run Llava
We also provide an example to get the result of LLaVA, please go check `run_llava.py`.

By setting up the env for llava via following steps:

Step 1:
```
git clone https://github.com/haotian-liu/LLaVA.git
cd LLaVA
```
Step 2:
```
conda create -n llava python=3.10 -y
conda activate llava
pip install --upgrade pip  # enable PEP 660 support
git fetch --tags  
git checkout tags/v1.1.3  
pip install -e .
```

The above will install llava (1.5 only) and corresponding correct transformers version.
Then by installing `datasets` packages from huggingface (i.e., `pip install datasets`), you can run llava with the following command:

```
CUDA_VISIBLE_DEVICES=0 nohup python run_llava.py \
--output_path example_outputs/llava1.5_13b_val.json \
--model_path liuhaotian/llava-v1.5-13b \
--config_path configs/llava1.5.yaml
```

Then you can evaluate the results via the very first pipeline.
