#!/bin/bash
pyenv install 3.10.4
pyenv virtualenv 3.10.4 tweet_import_3.10.4
pip install --upgrade pip
pip install -r requirements.txt
