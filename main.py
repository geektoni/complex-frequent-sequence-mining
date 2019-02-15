import argparse
import profile
import pstats

import os

import pickle

import logging

from ComplexPrefixSpan.Builder import Builder
from ComplexPrefixSpan.ComplexPrefixSpan import ComplexPrefixSpan

from ExperimentParser import ExperimentParser

from pymining import itemmining

from utils import count_occurences, frequent_itemset

if __name__ == "__main__":

    # Add a command line parser
    parser = argparse.ArgumentParser(description='Run Complex prefix span over database')
    parser.add_argument('dataset_path', nargs="?", type=str, default="./datasets/test_sample.csv",
                        help='Path to the csv file which holds the sequence dataset.')
    parser.add_argument('--min_support', type=float, default=0.3, help="Min support value which can be used.")
    parser.add_argument('--structure_type', type=str, default="binary_tree",
                        help="Specify which complex structure is contained in the sequences.")
    parser.add_argument('--max_length_sequence', type=int, default=10, help="Maximal length of the frequent sequences.")
    parser.add_argument('--iterative', action="store_true", default=False, help="Run using the iterative approach.")
    parser.add_argument('--hash', action="store_true", default=False, help="Run using the sha1 encode for items.")
    parser.add_argument('--cores', type=int, default=1, help="How many core we want to use.")
    parser.add_argument('--profile_execution', default=False, action="store_true", help="Take some performance measures.")
    parser.add_argument('--use_frequent_itemset', default=False, action="store_true", help="Use frequent itemset (to compare).")
    parser.add_argument('--jaccard_tresh', default=1.0, type=float, help="Jaccard Similarity treshold")
    parser.add_argument("--output_dir", default="./results/", type=str, help="Output dir for the results")
    parser.add_argument("--experiments", default="", type=str, help="Run the experiments using the config.")

    # Parse the command line arguments
    args = parser.parse_args()

    if args.experiments == "":
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
                result[1].sort()
                print(count_occurences(result[1], args.max_length_sequence))
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
    else:

        logger = logging.getLogger("performance_logger")
        file_handler = logging.FileHandler("./experiments/performance_5.csv")
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

        exp_parser = ExperimentParser(dict(), "./experiments.conf")
        args_e = exp_parser.parse()

        number_of_min=""
        for i in range(1, 50+1):
            number_of_min += str(i)+","
        number_of_min = number_of_min[0:len(number_of_min)-1]

        logger.info("algorithm,database_size,max_tree_size,max_sequence_size,jaccard_tresh,min_support,time,total_frequent_patterns,"+number_of_min)

        for alg in args_e["algorithms"]:
            for d_size in args_e["database_size"]:
                for m_tree in args_e["max_tree_size"]:
                    for m_seq in args_e["max_sequence_size"]:
                        for ms in args_e["min_support"]:
                            for j in args_e["jaccard_tresh"]:

                                # Use frequent itemset only with equality
                                if alg == "frequent" and float(j) != 1.0:
                                    continue

                                # Database name
                                dataset_name = "./datasets/dataset_"+d_size+"_"+m_tree+"_"+m_seq+".csv"

                                # Build the dataset
                                print("[*] Building the dataset.")
                                if args.structure_type == "synthea":
                                    dataset = Builder.create_from_synthea(args.dataset_path)
                                else:
                                    dataset = Builder.create_dataset(dataset_name)

                                # Build a new dataset using hashes instead of the plain sequences
                                if args.hash:
                                    print("[*] Building the hash version of the dataset.")
                                    dataset, hashDict = Builder.create_hash_dataset(dataset)

                                # Generate the name of the output file
                                if not alg == "frequent":
                                    output_result = os.path.splitext(os.path.basename(dataset_name))[0] + "_" + str(
                                        int(args.jaccard_tresh * 100)) \
                                                    + "_" + str(int(float(ms)*100)) + "_" + str(args.max_length_sequence) + ".db"
                                else:
                                    output_result = os.path.splitext(os.path.basename(dataset_name))[0] + "_frequentitems_" \
                                                    + str(int(float(ms)*100)) + ".db"

                                if not alg == "frequent":
                                    # Find complex sequences
                                    print("[*] Executing Prefix Span algorithm on {} cores on dataset {}".format(args.cores, dataset_name))

                                    finder = ComplexPrefixSpan(dataset, int(args.cores), float(j))
                                    result = finder.compute(float(ms), int(m_seq), args.iterative)

                                    final_string = "{},{},{},{},{},{},{},{},".format(alg, d_size, m_tree, m_seq, j, ms, result[0], len(result[1]))

                                    for e in count_occurences(result[1], 50):
                                        final_string += str(e)+","
                                    final_string = final_string[0:len(final_string)-1]
                                    logger.info(final_string)


                                    #result[1].sort()
                                    #print(result[1])
                                else:
                                    print("[*] Execution Frequent Itemset algorithm on dataset {}".format(dataset_name))
                                    relim_input = itemmining.get_relim_input(dataset)
                                    result = frequent_itemset(relim_input, float(ms)*len(dataset))

                                    final_string = "{},{},{},{},{},{},{},{},".format(alg, d_size, m_tree, m_seq, j, ms, result[0],
                                                                                  len(result[1]))

                                    for e in count_occurences(result[1], 50):
                                        final_string += str(e) + ","
                                    final_string = final_string[0:len(final_string) - 1]
                                    logger.info(final_string)

                                # Save the file to disk
                                with open(args.output_dir + output_result, "wb") as f:
                                    pickle.dump(result[1], f)
