import argparse

from ComplexPrefixSpan.Builder import Builder
from ComplexPrefixSpan.ComplexPrefixSpan import ComplexPrefixSpan
from ComplexPrefixSpan.Sequence import *

if __name__ == "__main__":

    # Add a command line parser
    parser = argparse.ArgumentParser(description='Run Complex prefix span over database')
    parser.add_argument('dataset_path', nargs="?", type=str, default="./datasets/test_sample.csv",
                        help='Path to the csv file which holds the sequence dataset.')
    parser.add_argument('--min_support', type=int, default=2, help="Min support value which can be used.")
    parser.add_argument('--structure_type', type=str, default="binary_tree",
                        help="Specify which complex structure is contained in the sequences.")

    # Parse the command line arguments
    args = parser.parse_args()

    # Build the dataset
    dataset = Builder.create_dataset(args.dataset_path)

    database = [
        Sequence([SequenceItem(1), SequenceItem(2), SequenceItem(3)]),
        Sequence([SequenceItem(3), SequenceItem(3), SequenceItem(9)]),
        Sequence([SequenceItem(3), SequenceItem(3), SequenceItem(3)]),
    ]

    seqs =  [
        Sequence([SequenceItem(1), SequenceItem(2), SequenceItem(3)]),
        Sequence([SequenceItem(3), SequenceItem(3)])]

    # Find complex sequences
    finder = ComplexPrefixSpan(dataset)
    result = finder.compute_frequent_complex_patterns(args.min_support, 3)
    print(result)
