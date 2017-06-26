#!/bin/bash

python3 -m venv "/Users/pcadiot/Piscine-Python/day03/ex01/local_lib"

# virtualenv /Users/pcadiot/Piscine-Python/day03/ex01/local_lib
pip3 --version

pip3 install --log fichier.log --upgrade --force-reinstall  git+https://github.com/jaraco/path.py.git

python3 my_program.py