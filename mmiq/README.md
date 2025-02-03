# Evaluation Guidelines
To execute our evaluation script, please ensure that the structure of your model outputs is the same as ours.

There are two evaluation methods:
1. Evaluation only
2. Parsing and evaluation

## Evaluation Only
You need to put all the outputs into *one file* in the following format by using your own answer-parsing program:

```
{
    "data_id": "0",
    "category": "Temporal Movement",
    "parsed_pred": "A" 
},

{
    "data_id": "1",
    "category": "Temporal Movement",
    "parsed_pred": "D"
},

```


Then run eval_only with:
```
python main_eval_only.py --output_path ./example_outputs/example_output_parsed.jsonl --answer_path ./MMIQ_benchmark_answer_dict.jsonl
```

Please refer to [example output](https://github.com/AceCHQ/MMIQ/blob/main/mmiq/example_outputs/example_output_parsed.jsonl) for a detailed prediction file form.


## Parse and Evaluation
You can also provide the LMM's responses and run the `main_parse_and_eval.py` to execute our answer-parsing program as below:

### Output file
```
    {
        "data_id": "0",
        "category": "Temporal Movement",
        "response": "The most appropriate option to fill in the question mark is option A." # model response
    },

    {
        "data_id": "1",
        "category": "Temporal Movement",
        "response": "The most appropriate option is D" # model response
    },
    ...
```

Please refer to [example output](https://github.com/AceCHQ/MMIQ/blob/main/mmiq/example_outputs/example_model_output/output_example.jsonl) for a correct form of the prediction file.

### Evaluation
```
python main_parse_and_eval.py --output_path ./example_outputs/example_model_output/output_example.jsonl --answer_path ./MMIQ_benchmark_answer_dict.jsonl            
```

`main_parse_and_eval.py` will generate `result.json` under the same folder as `output_path`.

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
We also provide an example to get the result of LLaVA, please check `run_llava.py`.

Setting up the env for llava via the following steps:

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

The above will install llava (1.5 only) and the corresponding transformers version.
Then by installing `datasets` packages from the huggingface (i.e., `pip install datasets`), you can run llava with the following command:

```
CUDA_VISIBLE_DEVICES=0 nohup python run_llava.py \
--output_path example_outputs/llava1.5_13b_val.json \
--model_path liuhaotian/llava-v1.5-13b \
--config_path configs/llava1.5.yaml
```

Then you can evaluate the results via the aforementioned evaluation pipeline.
