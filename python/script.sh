#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Step 1: Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Step 2: Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Step 3: Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Step 4: Install requirements
echo "Installing requirements from requirements.txt..."
pip install -r requirements.txt

# Step 5: Confirmation
echo "Setup complete. Virtual environment 'venv' is ready and dependencies are installed."
echo "To activate the virtual environment, run: source venv/bin/activate"
