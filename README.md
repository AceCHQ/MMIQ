# MMIQ Benchmark

[**🌐 Homepage**](https://AceCHQ.github.io/MMIQ) | [**🏆 Leaderboard**](https://AceCHQ.github.io/MMIQ/#leaderboard) | [**🤗 MMIQ**](https://huggingface.co/datasets/MMIQ/) | [**📖 MMIQ arXiv**]() 

This repo contains the evaluation code for the paper "[MMIQ: Are Your Multimodal Large Language Models Smart Enough?](https://arxiv.org/abs/)"


## Introduction


###  MMIQ

MMIQ is a new benchmark designed to evaluate MLLMs' intelligence through multiple reasoning patterns demanding abstract reasoning abilities. It encompasses **three input formats, six problem configurations, and eight reasoning patterns**. With **2,710 samples**, MMIQ is the most comprehensive and largest AVR benchmark for evaluating the intelligence of MLLMs, and **3x and 10x** larger than two very recent benchmarks MARVEL and MathVista-IQTest, respectively. With MMIQ, we have conducted a comprehensive, quantitative evaluation of prominent MLLMs and present significant challenges: For example, the best-performing MLLM only achieves an average accuracy of 27.49%, slightly higher than randomly selecting an answer among four options. Notably, the accuracy of 75% reasoning patterns is lower than 30%. The best-performing MLLM falls short of human performance by 23.8%, as it often stucks in incorrect visual understanding and recognition of wrong pattern. This substantial gap highlights MLLMs' limitations in AVR tasks and underscores the necessity of our MMIQ. By focusing on AVR problems, MMIQ provides a targeted assessment of the cognitive capabilities and intelligence of MLLMs, contributing to a more comprehensive understanding of their strengths and limitations in the pursuit of artificial general intelligence (AGI).

<div align="center">
<img src="https://github.com/AceCHQ/MMIQ/blob/main/mmiq/MMIQ_distribution.png" width="50%">
</div>

## Dataset Creation

MMIQ is a new benchmark designed to evaluate MLLMs’ intelligence through multiple reasoning patterns demanding abstract reasoning abilities. It adopts data from professional and authoritative examinations and performs rigorous quality control, which ensures its correctness and validity. For more detailed information, please refer to our Hugging Face datasets:

- [**🤗 MMIQ Dataset**](https://huggingface.co/datasets/MMIQ/)

## Evaluation

Please refer to our evaluation folder for detailed information on evaluating with MMIQ benchmark:

- [**MMIQ Evaluation**](mmiq)

🎯 **MMIQ Evaluation**

- **We have released MMIQ dataset with 2710 problems, across eight reasoning patterns.**
- **With our evaluation folder, you can use the MLLM's response or the parsed prediction as input to get the performance of MMIQ.**


## Disclaimers
The guidelines for the annotators emphasized strict compliance with copyright and licensing rules from the initial data source, specifically avoiding materials from websites that forbid copying and redistribution. 
Should you encounter any data samples potentially breaching the copyright or licensing regulations of any site, we encourage you to [contact](#contact) us. Upon verification, such samples will be promptly removed.

## Contact
- Huanqia Cai: caihuanqia19@mails.ucas.ac.cn

## Acknowledgment
Our code based on [MMMU](https://github.com/MMMU-Benchmark/MMMU). We thank the authors of MMMU for their great work and clean code.

