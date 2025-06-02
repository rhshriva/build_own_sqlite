#!/bin/bash

# Activate the virtual environment
echo "Activating virtual environment..."
source .my_venv/bin/activate

# Run all tests in the tests directory
echo "Running all tests in the tests directory..."
python -m unittest discover tests 