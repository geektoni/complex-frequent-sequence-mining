import argparse
import profile
import pstats

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
    parser.add_argument('--max_length_sequence', type=int, default=3, help="Maximal length of the frequent sequences.")
    parser.add_argument('--iterative', action="store_true", default=False, help="Run using the iterative approach.")
    parser.add_argument('--hash', action="store_true", default=False, help="Run using the sha1 encode for items.")
    parser.add_argument('--cores', type=int, default=1, help="How many core we want to use.")
    parser.add_argument('--profile_execution', default=False, action="store_true", help="Take some performance measures.")

    # Parse the command line arguments
    args = parser.parse_args()

    # Build the dataset
    print("[*] Building the dataset.")
    dataset = Builder.create_dataset(args.dataset_path)

    # Build a new dataset using hashes instead of the plain sequences
    if args.hash:
        print("[*] Building the hash version of the dataset.")
        dataset, hashDict = Builder.create_hash_dataset(dataset)

    database = [
        Sequence([SequenceItem(1), SequenceItem(2), SequenceItem(3)]),
        Sequence([SequenceItem(3), SequenceItem(3), SequenceItem(9)]),
        Sequence([SequenceItem(3), SequenceItem(3), SequenceItem(3)]),
    ]

    seqs =  [
        Sequence([SequenceItem(1), SequenceItem(2), SequenceItem(3)]),
        Sequence([SequenceItem(3), SequenceItem(3)])]

    # Find complex sequences
    print("[*] Executing Prefix Span algorithm on {} cores".format(args.cores))

    finder = ComplexPrefixSpan(dataset, int(args.cores))
    if not args.profile_execution:
        result = finder.compute(args.min_support, args.max_length_sequence, args.iterative)
        print(result)
    else:
        profile.run("finder.compute(args.min_support, args.max_length_sequence, args.iterative)", "prefix_span.stat")
        p = pstats.Stats('prefix_span.stat')
        p.strip_dirs().sort_stats(-1).print_stats()

