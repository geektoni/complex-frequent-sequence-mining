import argparse
import profile
import pstats

import os

import pickle

from ComplexPrefixSpan.Builder import Builder
from ComplexPrefixSpan.ComplexPrefixSpan import ComplexPrefixSpan

from pymining import itemmining

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
    parser.add_argument('--use_frequent_itemset', default=False, action="store_true", help="Use frequent itemset (to compare).")
    parser.add_argument('--jaccard_tresh', default=1.0, type=float, help="Jaccard Similarity treshold")
    parser.add_argument("--output_dir", default="./results/", type=str, help="Output dir for the results")

    # Parse the command line arguments
    args = parser.parse_args()

    # Build the dataset
    print("[*] Building the dataset.")
    if args.structure_type == "synthea":
        dataset = Builder.create_from_synthea(args.dataset_path)
    else:
        dataset = Builder.create_dataset(args.dataset_path)

    # Build a new dataset using hashes instead of the plain sequences
    if args.hash:
        print("[*] Building the hash version of the dataset.")
        dataset, hashDict = Builder.create_hash_dataset(dataset)

    # Generate the name of the output file
    if not args.use_frequent_itemset:
        output_result = os.path.splitext(os.path.basename(args.dataset_path))[0]+"_"+str(int(args.jaccard_tresh*100))\
                        +"_"+str(args.min_support)+"_"+str(args.max_length_sequence)+".db"
    else:
        output_result = os.path.splitext(os.path.basename(args.dataset_path))[0] + "_frequentitems_"\
                        + str(args.min_support) + ".db"

    if not args.use_frequent_itemset:
        # Find complex sequences
        print("[*] Executing Prefix Span algorithm on {} cores".format(args.cores))

        finder = ComplexPrefixSpan(dataset, int(args.cores), args.jaccard_tresh)
        if not args.profile_execution:
            result = finder.compute(args.min_support, args.max_length_sequence, args.iterative)
            #result[1].sort()

            print(result[1])
        else:
            result = profile.run("finder.compute(args.min_support, args.max_length_sequence, args.iterative)", "prefix_span.stat")
            p = pstats.Stats('prefix_span.stat')
            p.strip_dirs().sort_stats(-1).print_stats()
    else:
        print("[*] Execution Frequent Itemset algorithm.")
        relim_input = itemmining.get_relim_input(dataset)
        result = itemmining.relim(relim_input, min_support=args.min_support)
        print(result[1])

    # Save the file to disk
    with open(args.output_dir+output_result, "wb") as f:
        pickle.dump(result[1], f)

