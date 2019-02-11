import argparse
import pickle

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Compare results between algorithms')
    parser.add_argument("first_file", type=str, help="First result we want to compare")
    parser.add_argument("second_file", type=str, help="Second result we want to compare")

    args = parser.parse_args()

    with open(args.first_file, "rb") as f:
        result_a = pickle.load(f)
        print(result_a)

    with open(args.second_file, "rb") as f:
        result_b = pickle.load(f)
        print(result_b)

    set_inter = set(result_a).intersection(result_b)
    set_union = set(result_a + result_b)

    print("Intersection: {}".format(set_inter))

    inter = len(list(set_inter))
    union = len(list(set_union))
    print(float(inter / union))

