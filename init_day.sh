#!/usr/bin/bash

while getopts d: flag
do
    case "$flag" in 
        d) day_num=${OPTARG};;
    esac
done

mkdir -p "day$day_num"
cp ./base.py "day$day_num/day$day_num.py"
curl "https://adventofcode.com/2023/day/$day_num/input" -H "Cookie: session=$AOC_SESSION_ID" > "day$day_num/input.txt"
head -4 "day$day_num/input.txt" > "day$day_num/sample.txt"