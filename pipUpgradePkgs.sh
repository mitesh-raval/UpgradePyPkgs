#!/bin/bash

pip3 list -o > pkgs.txt
python3 utils/pkgs.py pkgs.txt upgrade.txt
pip3 install --upgrade -r upgrade.txt
