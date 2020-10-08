#!/bin/bash
cd application
git checkout master
git pull
pip3 install -r /home/flasky/starwarsV/requirements.txt
python3 server.py