#!/bin/bash

source env/bin/activate

python3 -m pip install --upgrade wheel | grep -v 'already satisfied'

python3 -m pip install -r requirements.txt | grep -v 'already satisfied'
