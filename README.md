# MM-IQ Benchmark

[**🌐 Homepage**](https://acechq.github.io/MMIQ-benchmark/) | [**🏆 Leaderboard**](https://acechq.github.io/MMIQ-benchmark/#leaderboard) | [**🤗 MM-IQ**](https://huggingface.co/datasets/huanqia/MMIQ) | [**📖 MM-IQ arXiv: Comming Soon**]() 

This repo provides the evaluation code of the [MM-IQ benchmark](https://acechq.github.io/MMIQ-benchmark/).


## Introduction

###  MM-IQ

MM-IQ is the most comprehensive and largest abstract visual reasoning (AVR) benchmark for evaluating MLLMs' intelligence levels through multiple reasoning patterns. It encompasses three input formats, six problem configurations, and eight reasoning patterns. MM-IQ consists of **2,710 samples** and is **3x** and **10x** larger than two recent benchmarks MARVEL and MathVista-IQTest, respectively. Through a quantitative evaluation using MM-IQ, we found that state-of-the-art MLLMs such as GPT-4o and Gemini only achieve an average accuracy of 27.49%, slightly higher than randomly selecting a single correct answer from four options.


## Dataset Curation
<div align="center">
<img src="https://acechq.github.io/MMIQ-benchmark/static/imgs/MMIQ_distribution.png" width="50%">
</div>

For more detailed information, please refer to [**MM-IQ Dataset**](https://huggingface.co/datasets/huanqia/MMIQ).

We have uploaded a demo to illustrate how to access the MM-IQ dataset on Hugging Face, available at [hugging_face_dataset_demo.ipynb](https://github.com/AceCHQ/MMIQ/blob/main/mmiq/jupyter_notebook_demos/hugging_face_dataset_demo.ipynb).

## Evaluation

Please refer to [**MM-IQ Evaluation**](mmiq) for more detailed information.


🎯 **MM-IQ Evaluation**

- **We have released MM-IQ dataset with 2710 problems, across eight reasoning patterns.**
- **With our evaluation folder, you can use the MLLM's response or the parsed prediction as input to get the performance of MM-IQ.**


## Disclaimers
The guidelines for the annotators emphasized strict compliance with copyright and licensing rules from the initial data source, specifically avoiding materials from websites that forbid copying and redistribution. 
If you encounter any data samples potentially breaching the copyright or licensing regulations of any site, we encourage you to [contact](#contact) us. Upon verification, such samples will be promptly removed.

## Contact
- Huanqia Cai: caihuanqia19@mails.ucas.ac.cn

## Acknowledgment
Our code is based on [MMMU](https://github.com/MMMU-Benchmark/MMMU). We thank the authors of MMMU for their great work and clean code.

