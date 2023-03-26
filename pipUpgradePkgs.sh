#!/bin/bash

pip3 list -o > pkgs.txt
python3 ./pkgNames.py pkgs.txt upgrade.txt
pip3 install --upgrade -r upgrade.txt
