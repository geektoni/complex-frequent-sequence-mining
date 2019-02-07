from binarytree import tree, bst, heap, build
import random
import csv

N_SEQUENCE = 10
MIN_RANGE_TREE_HEIGHT = 0
MAX_RANGE_TREE_HEIGHT = 4
MIN_RANGE_SEQ_LENGTH = 1
MAX_RANGE_SEQ_LENGTH = 10

for x in range(N_SEQUENCE):
    seq_range = random.randint(MIN_RANGE_SEQ_LENGTH,MAX_RANGE_SEQ_LENGTH)
    seq = []
    for y in range(seq_range):
        tree_height = random.randint(MIN_RANGE_TREE_HEIGHT,MAX_RANGE_TREE_HEIGHT)
        my_tree = tree(tree_height)
        seq.append(my_tree.values)
        
    #print("%s; %s\n" % (x,';'.join(str(e) for e in seq)))
    with open('dataset.txt', 'aw') as csvfile:
        csvfile.write("%s; %s\r\n" % (x,';'.join(str(e) for e in seq)))