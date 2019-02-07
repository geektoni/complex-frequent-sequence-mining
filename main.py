from ComplexPrefixSpan.Builder import Builder
from ComplexPrefixSpan.ComplexPrefixSpan import ComplexPrefixSpan
from ComplexPrefixSpan.SequenceItem import *
from ComplexPrefixSpan.Sequence import *

if __name__ == "__main__":

    database = [
        Sequence([SequenceItem(1), SequenceItem(2), SequenceItem(3)]),
        Sequence([SequenceItem(3), SequenceItem(3), SequenceItem(9)]),
        Sequence([SequenceItem(3), SequenceItem(3), SequenceItem(3)]),
    ]

    seqs =  [
        Sequence([SequenceItem(1), SequenceItem(2), SequenceItem(3)]),
        Sequence([SequenceItem(3), SequenceItem(3)])]


    dataset = Builder.create_dataset("./datasets/test_sample.csv")

    finder = ComplexPrefixSpan(database)
    result = finder.compute_frequent_complex_patterns(1, 3)
    print(result)
