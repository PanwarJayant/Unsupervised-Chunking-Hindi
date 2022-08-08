# NLP Final Report: Unsupervised Algorithm for Chunking in Indian Languages

This README file describes the files present in this folder, and running instructions for the submitted algorithm.

## Contents

- Final_Project_Presentation - Presentation file for final evaluations
- Final_Project_Report - Detailed report on the work done during the entirety of the Project
- **Base** repo - Contains all code and corpus used for developing Base model. Also contains the gold standard file used for evaluating both base and base++ model
- **Base++** repo - Contains all code and corpus used for developing Base++ model

## Base Repo Contents

- kmeans.py - Main code file containing the algorithm
- gold.py - Code to run evaluations
- chunks.txt - Actual chunks formed midway
- dataset.txt - The dataset used to run the algorithm. Contains sentences in Hindi tagged with their respective POS Tags
- gold_standard.txt - The gold standard for the dataset used in order to run evaluations
- sample.txt - A sample file of chunks of certain sentences
- logs.txt - Debugging outputs

## Usage for Base Model (K Means Algorithm)

In order to run the K Means algorithm. run the following command in the root folder

```bash
python3 kmeans.py
```

This will generate a `output.txt` file containing the chunks.

In order to run the evaluation, run

```bash
python3 gold.py
```

This will give us accuracy by printing them on the terminal.

## Base++ Repo Contents

- hierarchical.ipynb - Python notebook containing the code for Base++ (Hierarchical Clustering Algorithm) Model
- hierarchical_corpus.txt - Text file containing the corpus (one sentence only) for running hierarchical.ipynb

## Usage for Base++ Model (Hierarchical Algorithm)

- Since the code is a python notebook, the code blocks can be run individually step by step.
- Make sure to do appropriate changes for incorporating the corpus. The current code has path to Google Drive for fetching the hierarchical_corpus.txt
- Finally, make sure to have necessary libraries installed if running locally: numpy, nltk, matplotlib, scipy, sklearn

### By: Jayant Panwar (2019114013), Prajneya Kumar (2019114011)
