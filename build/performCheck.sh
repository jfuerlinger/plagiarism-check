#!/bin/bash
unzip /input/*.zip -d ./submissions
python ./checkPlagiat.py

# for dev purposes
cp ./*.xlsx /input/
# /bin/bash


