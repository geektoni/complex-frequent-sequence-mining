"""
This class obtain from a file the sequence dataset and it
builds a representation use
"""
from ComplexPrefixSpan.SequenceItem import SequenceItem
from ComplexPrefixSpan.Sequence import Sequence


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

