#!/bin/bash

source env/bin/activate

pip3 install -r requirements.txt | grep -v 'already satisfied'
