"""Utils for data load, save, and process (e.g., prompt construction)"""

import os
import json
import yaml
import re


REASONING_PATTERN = ["Temporal Movement", "2D-Geometry", "3D-Geometry", "Logical Operation", "Mathematical", "Spatial Relationship", "Visual Instruction", "Concrete Object"]

# DATA SAVING
def save_json(filename, ds):
    with open(filename, 'w') as f:
        json.dump(ds, f, indent=4)

def load_yaml(file_path):
    with open(file_path, 'r') as stream:
        try:
            yaml_dict = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return yaml_dict

def parse_img_path(text):
    matches = re.findall("<img='(.*?)'>", text)
    return matches

def process_single_sample(data):
    question = data['question']
    return {'id': data['data_id'], 'question': question, 'answer': data['answer'], 'image': data['image']}


# DATA SAVING
def save_json(filename, ds):
    with open(filename, 'w') as f:
        json.dump(ds, f, indent=4)

def save_jsonl(filename, data):
    """
    Save a dictionary of data to a JSON Lines file with the id as key and the response dict as value.

    Args:
        filename (str): The path to the file where the data should be saved.
        data (dict): The dictionary containing the data to save where key is the id and value is the response dict.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for idx, single_data in data.items():
            # Extract the base filename without the extension
            # Create a JSON object with the filename as the key and caption as the value
            json_record = json.dumps(single_data, ensure_ascii=False)
            # Write the JSON object to the file, one per line
            f.write(json_record + '\n')

def save_args(args, path_dir):
    argsDict = args.__dict__
    with open(path_dir + 'setting.txt', 'w') as f:
        f.writelines('------------------ start ------------------' + '\n')
        for eachArg, value in argsDict.items():
            f.writelines(eachArg + ' : ' + str(value) + '\n')
        f.writelines('------------------- end -------------------')


# DATA PROCESSING
def construct_prompt(sample, config):
    question = sample['question']
    example = ""
    res_dict = {}
    res_dict['correct_choice'] = sample['answer']
    res_dict['final_input_prompt'] = question
    res_dict.update(sample)
    return res_dict
