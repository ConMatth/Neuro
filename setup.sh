#!/bin/bash

# Check if virtual environment folder exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

echo "Setup complete. Virtual environment is ready and dependencies are installed."
