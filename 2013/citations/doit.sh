#!/bin/bash
echo -n "" > output.csv
awk '{system("python citations.py -y " $1 " -p " $2 " >> output.csv")}' inputs.txt

