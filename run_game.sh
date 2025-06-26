#!/bin/bash

# Optional: Set up a virtual environment (if you want to use one)
# python3 -m venv venv
# source venv/bin/activate

# install dependencies from requirements.txt
pip install -r requirements.txt

python3 -m pip install pygame-menu

# Run the game
python3 code/main.py
