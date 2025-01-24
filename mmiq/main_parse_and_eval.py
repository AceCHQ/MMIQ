"""Parse and Evalate"""
import os
import json

import pdb
from argparse import ArgumentParser

from utils.data_utils import save_json, REASONING_PATTERN
from utils.eval_utils import evaluate, parse_multi_choice_response, calculate_ins_level_acc


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--output_path', type=str, default="./output_example.jsonl", help="The path to model output file.")
    parser.add_argument('--answer_path', type=str, default="./MMIQ_benchmark.jsonl", help="Answer file path.")
    args = parser.parse_args()

    
    with open(args.output_path, 'r') as f:
        output_data = f.readlines()
    
    with open(args.answer_path, 'r') as f:
        answer_data = f.readlines()

    output_dict_w_cat = {}
    for idx in range(len(output_data)):
        tmp_data = json.loads(output_data[idx])
        category = tmp_data["category"]
        if category not in output_dict_w_cat:
            output_dict_w_cat.update({category: {}})
        data_id = tmp_data["data_id"]
        parsed_pred = parse_multi_choice_response(tmp_data["response"])
        output_dict_w_cat[category].update({data_id: parsed_pred})
     
    num = 0
    for category in output_dict_w_cat:
        num += len(output_dict_w_cat[category])
    # group by category
    answer_dict_w_cat = {}
    for idx in range(len(answer_data)):
        tmp_data = json.loads(answer_data[idx])
        category = tmp_data["category"]
        if category not in answer_dict_w_cat:
            answer_dict_w_cat.update({category: {}})
        data_id = tmp_data["data_id"]
        ground_truth = tmp_data["answer"]
        answer_dict_w_cat[category].update({data_id: ground_truth})

    evaluation_result = {}

    sample_num = 0

    for category in REASONING_PATTERN:
    #for category in output_dict_w_cat:
        #print("Evaluating: {}".format(category))
        # get cat_outputs and cat_answers
        try:
            cat_outputs = output_dict_w_cat[category]
            cat_answers = answer_dict_w_cat[category]
        except KeyError:
            print("Skipping {} for not found".format(category))
            continue
        
        exampels_to_eval = []
        for data_id, parsed_pred in cat_outputs.items():
            exampels_to_eval.append({
                "id": data_id,
                "answer": cat_answers[int(data_id)],
                "parsed_pred": parsed_pred
            })
            sample_num += 1            
        judge_dict, metric_dict = evaluate(exampels_to_eval)
        metric_dict.update({"num_example": len(exampels_to_eval)})
        evaluation_result[category] = metric_dict

    printable_results = {}
    print("Accuracy of Reasoning Pattern of MMIQ:")
    for category in evaluation_result:
        print(category, ":", round(evaluation_result[category]["acc"], 3))
    # pdb.set_trace()
    # table.append(["-----------------------------", "-----", "----"])
    all_ins_acc = calculate_ins_level_acc(evaluation_result)
    if sample_num < 2710:
        print("Warning: The evaluation input file is not complete.")
    printable_results['Overall'] = {"MMIQ": 2710, "evaluation num": sum([cat_results['num_example'] for cat_results in evaluation_result.values()]),
                                    "acc": round(all_ins_acc, 5)
                                    }
    print(printable_results)
    evaluation_result["Overall"] = {"evaluation num": sum([cat_results['num_example'] for cat_results in evaluation_result.values()]),"acc": round(all_ins_acc, 5)}
    save_json(os.path.join(os.path.dirname(args.output_path), 'result.json'), evaluation_result)
    print("Evaluation results are saved in", os.path.join(os.path.dirname(args.output_path), 'result.json'))

