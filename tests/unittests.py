import unittest

from ComplexPrefixSpan.ComplexPrefixSpan import ComplexPrefixSpan
from ComplexPrefixSpan.SequenceItem import *
from ComplexPrefixSpan.Sequence import *

database = [
        Sequence([SequenceItem(1), SequenceItem(1), SequenceItem(3)]),
        Sequence([SequenceItem(3), SequenceItem(3), SequenceItem(9)]),
        Sequence([SequenceItem(3), SequenceItem(3), SequenceItem(3)]),
    ]
seqs =  [
        Sequence([SequenceItem(1), SequenceItem(2), SequenceItem(3)]),
        Sequence([SequenceItem(3), SequenceItem(3)])]

class TestComplexPrefixSpan(unittest.TestCase):

    def test_one_length_support(self):
        matcher = ComplexPrefixSpan(database)
        result = matcher.one_length_seq_patterns(2)
        self.assertEqual(result, {"1":2, "3":6})


if __name__ == "__main__":
    unittest.main()
