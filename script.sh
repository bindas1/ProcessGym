#!/bin/bash

# Specify the Python script to run
python_script="dqn_learning.py"

# Number of times to run the Python script
num_runs=30

# Loop to run the script multiple times for recreation
for ((i=1; i<=$num_runs; i++)); do
    echo "Running iteration $i"
    python "$python_script" recreation

# Loop to run the script multiple times for extension (running example)
for ((i=1; i<=$num_runs; i++)); do
    echo "Running iteration $i"
    python "$python_script" extension
done
