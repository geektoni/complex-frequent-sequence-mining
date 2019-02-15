#!/bin/bash
declare -a listN=("1000" "2000" "5000")
declare -a listH=("4" "6")
declare -a listS=("10" "20")
for i in "${listN[@]}"
do
	for j in "${listH[@]}"
	do
		for k in "${listS[@]}"
		do
		   python3 dataset_generator.py --n_sequence="$i" --common_freq=0.3 --max_range_tree_height="$j" --max_range_seq_length="$k" --common_sequence=1
		done
	done
done
