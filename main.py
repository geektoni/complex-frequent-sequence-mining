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

    finder = ComplexPrefixSpan(database)
    print(finder.one_length_seq_patterns(1))
    #print(finder.support(seqs))

