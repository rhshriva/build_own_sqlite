#!/bin/bash

# Create a virtual environment in .venv
echo "Creating virtual environment..."
python3 -m venv .my_venv

# Activate the virtual environment
echo "Activating virtual environment..."
source .my_venv/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. To activate the environment later, run:"
echo "source .my_venv/bin/activate" 