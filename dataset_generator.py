from binarytree import tree, bst, heap, build
import random
import csv
import argparse
if __name__ == "__main__":

    # Add a command line parser
    parser = argparse.ArgumentParser(description='Generate a dataset compsed by sequences of trees')
    parser.add_argument('dataset_file', nargs="?", type=str, default="./datasets/dataset.txt", help='Path to the output file')
    parser.add_argument('--n_sequence', type=int, default=10, help="Number of sequence to generate for the dataset")
    parser.add_argument('--min_range_tree_height', type=int, default=0, help="Minimum value for the height of the tree")
    parser.add_argument('--max_range_tree_height', type=int, default=4, help="Minimum value for the height of the tree")
    parser.add_argument('--min_range_seq_length', type=int, default=1, help="Minimum value for the height of the tree")
    parser.add_argument('--max_range_seq_length', type=int, default=10, help="Minimum value for the height of the tree")

    # Parse the command line arguments
    args = parser.parse_args()

    DATASET_FILE = args.dataset_file
    N_SEQUENCE = args.n_sequence
    MIN_RANGE_TREE_HEIGHT = args.min_range_tree_height
    MAX_RANGE_TREE_HEIGHT = args.max_range_tree_height
    MIN_RANGE_SEQ_LENGTH = args.min_range_seq_length
    MAX_RANGE_SEQ_LENGTH = args.max_range_seq_length
    for x in range(N_SEQUENCE):
	    seq_range = random.randint(MIN_RANGE_SEQ_LENGTH,MAX_RANGE_SEQ_LENGTH)
	    seq = []
	    for y in range(seq_range):
	        tree_height = random.randint(MIN_RANGE_TREE_HEIGHT,MAX_RANGE_TREE_HEIGHT)
	        my_tree = tree(tree_height)
	        seq.append(my_tree.values)
	        
	    #print("%s; %s\n" % (x,';'.join(str(e) for e in seq)))
	    with open(DATASET_FILE, 'a') as file:
	        file.write("%s; %s\r\n" % (x,';'.join(str(e) for e in seq)))