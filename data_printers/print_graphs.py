import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from ExperimentParser import ExperimentParser

font = {'size'   : 14}

matplotlib.rc('font', **font)

_file ="./experiments/performance_3.csv"

df = pd.read_csv(_file)

exp_parser = ExperimentParser(dict(), "./experiments.conf")
args_e = exp_parser.parse()

initial = 221
counter=0
base = 221

total_lines = []

#plt.figure(figsize=(12,8))

for d_size in args_e["database_size"]:
    for m_tree in args_e["max_tree_size"]:
        for m_seq in args_e["max_sequence_size"]:
            print(base+counter)
            plt.subplot(base+counter)
            counter += 1
            if (counter >= 4):
                counter = 0
                base = initial-10

            plt.title("dataset_{}_{}_{}".format(d_size, m_tree, m_seq))
            plt.yscale("log")
            plt.xlabel("Min Support")
            plt.ylabel("Time (ms)")

            for alg in args_e["algorithms"]:
                for j in args_e["jaccard_tresh"]:

                    if alg == "frequent" and j != "1":
                        continue

                    data = df[(df["algorithm"] == alg)
                    & (df["database_size"]==int(d_size))
                    & (df["max_tree_size"]==int(m_tree))
                    & (df["max_sequence_size"]==int(m_seq))
                    & (df["jaccard_tresh"] == float(j))]

                    if (alg == "prefix"):
                        label = "Prefix Span (Jaccard Tresh "+j+")"
                    else:
                        label = "Frequent Itemset"


                    l, = plt.plot(range(0, len(data["time"])), data["time"], "-o", label=label)
                    if (len(total_lines) < 3):
                        total_lines.append(l)

            plt.xticks(np.arange(0, 6), ("1", "0.75", "0.5", "0.33", "0.25", "0.2"))
plt.figlegend(total_lines, ("Prefix Span (J=1)", "Prefix Span (J=0.7)", "FP-Growth"), "lower center", ncol=3)
plt.tight_layout()
plt.show()
