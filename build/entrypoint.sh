#!/bin/bash
unzip /input/*.zip -d ./submissions
python ./checkPlagiat.py

# for dev purposes
cp -r ./submissions /input/submissions
cp ./*.xlsx /input
# /bin/bash


