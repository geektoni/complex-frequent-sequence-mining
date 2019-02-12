from binarytree import tree, bst, heap, build
import random
import csv
import argparse
import sys

if __name__ == "__main__":
##################################################################
    parser = argparse.ArgumentParser(description='Generate a dataset compsed by sequences of trees')
    parser.add_argument('dataset_dir', nargs="?", type=str, default="./datasets/", help='Path to the output file')
    parser.add_argument('--n_sequence', type=int, default=10, help="Number of sequence to generate for the dataset")
    parser.add_argument('--min_range_tree_height', type=int, default=0, help="Minimum value for the height of the tree")
    parser.add_argument('--max_range_tree_height', type=int, default=4, help="Minimum value for the height of the tree")
    parser.add_argument('--min_range_seq_length', type=int, default=1, help="Minimum value for the height of the tree")
    parser.add_argument('--max_range_seq_length', type=int, default=10, help="Minimum value for the height of the tree")
    parser.add_argument('--common_freq', type=float, default=1/10, help="the frequency of common elements [from 0 to 1]")
    parser.add_argument('--common_sequence', type=int, default=0, help="Generate a dataset with N common sequence")
    args = parser.parse_args()
##################################################################
    DATASET_DIR = args.dataset_dir
    N_SEQUENCE = args.n_sequence
    MIN_RANGE_TREE_HEIGHT = args.min_range_tree_height
    MAX_RANGE_TREE_HEIGHT = args.max_range_tree_height
    MIN_RANGE_SEQ_LENGTH = args.min_range_seq_length
    MAX_RANGE_SEQ_LENGTH = args.max_range_seq_length
    PARTICIPATION_FREQ = args.common_freq
    COMMON_SEQUENCE_N = args.common_sequence
    E_SEQUENCE = N_SEQUENCE
    COMMON_SEQUENCE = []
##################################################################
    if COMMON_SEQUENCE_N>0:
        if N_SEQUENCE*PARTICIPATION_FREQ>=COMMON_SEQUENCE_N:
            for x in range(COMMON_SEQUENCE_N):
                E_SEQUENCE = E_SEQUENCE - int(N_SEQUENCE * PARTICIPATION_FREQ)
        else:
            print('Common sequence number to high for that frequency/total number of sequence.')
            sys.exit()
##################################################################
    dataset = []
    for x in range(E_SEQUENCE):
	    seq_range = random.randint(MIN_RANGE_SEQ_LENGTH,MAX_RANGE_SEQ_LENGTH)
	    seq = []
	    for y in range(seq_range):
	        tree_height = random.randint(MIN_RANGE_TREE_HEIGHT,MAX_RANGE_TREE_HEIGHT)
	        my_tree = tree(tree_height)
	        seq.append(my_tree.values)
	    dataset.append(seq)
##################################################################
    c_dataset = []
    for x in range(COMMON_SEQUENCE_N):
        seq_range = random.randint(MIN_RANGE_SEQ_LENGTH,MAX_RANGE_SEQ_LENGTH)
        c_seq = []
        for y in range(seq_range):
            tree_height = random.randint(MIN_RANGE_TREE_HEIGHT,MAX_RANGE_TREE_HEIGHT)
            my_tree = tree(tree_height)
            c_seq.append(my_tree.values)
        c_dataset.append(c_seq)
##################################################################
    while len(dataset)<N_SEQUENCE:
        dataset.extend(c_dataset)
    random.shuffle(dataset)
##################################################################
    dataset_name = "dataset_"+str(N_SEQUENCE)+"_"+str(MAX_RANGE_TREE_HEIGHT)+"_"+str(MAX_RANGE_SEQ_LENGTH)+".csv"
    for x in range(N_SEQUENCE):
	    with open(DATASET_DIR + dataset_name, 'a') as file:
	        file.write("%s; %s\r\n" % (x,';'.join(str(e) for e in dataset[x])))