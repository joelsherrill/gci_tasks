#!/bin/bash
rm *.csv
awk '{system("python citations.py -y " $1 " -p " $2 " >> " $1 ".csv")}' inputs.txt

