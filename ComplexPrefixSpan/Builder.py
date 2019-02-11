"""
This class obtain from a file the sequence dataset and it
builds a representation use
"""
from ComplexPrefixSpan.SequenceItem import SequenceItem
from ComplexPrefixSpan.Sequence import Sequence
import hashlib 

import pandas as pd

class Builder:

    def __init__(self):
        pass

    @staticmethod
    def create_dataset(dataset_path) -> list:
        """
        Create a list of sequences from a given dataset
        :param dataset_path: the dataset file path
        :return: a list of sequences
        """

        # The list which will contain the various sequences
        dataset = []

        # Read the datafile and create the list with all
        # the structures
        with open(dataset_path) as f:
            for line in f:
                # [0] Id of the sequence
                # [1..n] list of sequence's items
                result = line.split(";")
                sequence = []
                for i in range(1, len(result)):
                    # Parse the sequence by removing the [,] chars
                    # and by substituing the None value with _
                    stripped = result[i].rstrip()
                    final = stripped.replace("[","").replace("]", "").replace("None", "_").replace(" ","")
                    sequence.append(SequenceItem(final))
                dataset += [Sequence(sequence)]

        return dataset

    @staticmethod
    def create_hash_dataset(dataset_no_hash):
        dataset = []
        hash_to_tree = dict()
        for row in dataset_no_hash:
            sequence = []
            for seqItem in row:
                gen = hashlib.sha1()
                gen.update(str(seqItem).encode("utf-8"))
                newItem = gen.hexdigest()
                hash_to_tree[newItem] = seqItem
                sequence.append(SequenceItem(newItem))
            dataset += [Sequence(sequence)]
        return dataset, hash_to_tree

    @staticmethod
    def create_from_synthea(dataset_path):

        result = []

        df = pd.read_csv(dataset_path)

        for p in df["PATIENT"].unique():
            seq = []
            df_p = df[df["PATIENT"]==p]
            for r in df_p.iterrows():
                item = []
                item.append(r[1]["DESCRIPTION"])
                item.append(r[1]["REASONDESCRIPTION"])
                seq.append(SequenceItem(item))
            result.append(Sequence(seq))

        return result
