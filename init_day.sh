#!/usr/bin/bash

while getopts d:y: flag
do
    case "$flag" in 
        d) day_num=${OPTARG};;
        y) year=${OPTARG};;
    esac
done

mkdir -p "./$year/day$day_num"
cp ./base.py "./$year/day$day_num/day$day_num.py"
curl "https://adventofcode.com/$year/day/$day_num/input" -H "Cookie: session=$AOC_SESSION_ID" > "./$year/day$day_num/input.txt"
head -4 "./$year/day$day_num/input.txt" > "./$year/day$day_num/sample.txt"