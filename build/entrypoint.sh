#!/bin/bash
unzip /input/*.zip -d ./submissions
python ./checkPlagiat.py

cp -r ./submissions /input/submissions
cp ./*.xlsx /input



