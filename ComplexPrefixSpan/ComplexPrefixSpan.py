"""
Class which implements the prefixSpan algorithm to mine
sequential pattern but extender in order to manage sequences
using complex data structures.
"""
class ComplexPrefixSpan:

    def __init__(self, database):
        self.database=database
        pass

    """
    Computes the k-frequent sequential patterns given the min support
    and return the result as a list. 
    """
    def compute_frequent_patterns(self, min_support, k) -> list:
        pass

    """
    Returns the projected database for a given suffix.
    """
    def project_database(self, suffix) -> list:
        return list(filter(lambda x: x.starts_with(suffix), self.database))


    """
    Compute the length-1 sequential patterns with support greater than k
    """
    def one_length_seq_patterns(self, k):
        support_set = dict()
        for s in self.database:
            for e in s:
                support_set[str(e)] = 1 if not str(e) in support_set else (support_set[str(e)]+1)
        return {i: v for i, v in support_set.items() if v >= k}


    """
    Compute the support value for a given set of sequences.
    It will return a dictionary with the supports count.
    """
    def support(self, sequences) -> dict:
        support_set = dict()
        for s in self.database:
            for seq in sequences:
                if s.contains(seq):
                    support_set[str(seq)] = 1 if not str(seq) in support_set else (support_set[str(seq)]+1)
        return support_set
