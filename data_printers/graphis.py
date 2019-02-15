import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

font = {'size'   : 14}

matplotlib.rc('font', **font)

fileRes = "experiments/performance.csv"

data = pd.read_csv(fileRes)

initial = 221
counter=0
base = 221
total_lines = []
plt.figure(figsize=(10,5))
for mss in set(data['max_sequence_size']):
    for mts in set(data['max_tree_size']):
        plt.subplot(base+counter)
        counter += 1
        if (counter >= 4):
            counter = 0
            base = initial-10
        for a in set(data['algorithm']):
            if a=="prefix":
                for jt in set(data['jaccard_tresh']):
                    data_s = data[(data['max_tree_size']==int(mts)) & (data['algorithm']==a) & (data['jaccard_tresh']==float(jt)) & (data['max_sequence_size']==int(mss))]
                    l, = plt.plot(range(0,len(data_s['time'])),data_s['time'],"-o",label="Prefix Span (J = {})".format(jt))
                    if len(total_lines)<3:
                                  total_lines.append(l)
            else:
                data_s = data[(data['max_tree_size']==int(mts)) & (data['algorithm']==a) & (data['max_sequence_size']==int(mss))]
                l, = plt.plot(range(0,len(data_s['time'])),data_s['time'],"-o",label="Frequent Itemset")
                if len(total_lines)<3:
                                  total_lines.append(l)
        plt.title("Max Sequence size = {} Max Tree size = {}".format(mss,mts))
        plt.yscale("log")
        plt.ylabel("Time (ms)")
        plt.xlabel("Dataset Size (# Transactions)")
        plt.xticks(np.arange(len(data_s["time"])), ('1000', '2000', '5000'))

plt.figlegend(total_lines, ("Prefix Span (J=1)", "Prefix Span (J=0.7)", "FP-Growth"), "lower center", ncol=3)
plt.tight_layout()
plt.savefig("mss_mts")
plt.show()
