"""
Class which implements the prefixSpan algorithm to mine
sequential pattern but extender in order to manage sequences
using complex data structures.
"""
from ComplexPrefixSpan.Sequence import Sequence
from ComplexPrefixSpan.SequenceItem import SequenceItem


class ComplexPrefixSpan:

    def __init__(self, database):
        self.database=database
        pass

    def compute_frequent_complex_patterns(self, min_support, k) -> list:
        return self._compute_frequent_patterns(min_support, k, self.database, None)

    """
    Computes the k-frequent sequential patterns given the min support
    and return the result as a list. 
    """
    def _compute_frequent_patterns(self, min_support, k, database, previous_frequent_item) -> list:

        # Frequent sequences found
        frequent_sequences = []

        # If k is less/equal than zero then we return an empty list,
        # since we reached the longest sequence size
        if k <= 0:
            return previous_frequent_item

        one_frequent = self.one_length_seq_patterns(min_support, database)

        # If the previous frequent item is none, then it means this is the
        # first run of the algorithm. Otherwise, create the new sets of newly
        # frequent items such to do projection.
        frequent_items = []
        if previous_frequent_item == None:
            for i, e in one_frequent.items():
                frequent_items.append(Sequence([e[1]]))
                frequent_sequences.append(Sequence([e[1]]))
        else:
            for i, e in one_frequent.items():
                tmp = previous_frequent_item.copy()
                tmp.append(e[1])
                frequent_items.append(tmp)

        # For each one-frequent patterns, we start mining recursively
        # all the others starting with it
        for e in frequent_items:
            projected_database_over_k = self.project_database(e, database)
            result = self._compute_frequent_patterns(min_support, k-1, projected_database_over_k, e)
            if (len(result) > 0):
                frequent_sequences += [result]
        return frequent_sequences

    """
    Returns the projected database for a given suffix.
    """
    def project_database(self, suffix, database) -> list:
        result = list(filter(lambda x: x.starts_with(suffix), database))
        return list(map(lambda x: x.suffix(len(suffix)), result))

    """
    Compute the length-1 sequential patterns with support greater than k
    """
    def one_length_seq_patterns(self, k, database):
        support_set = dict()
        for s in database:
            for e in s:
                support_set[str(e)] = (1, e) if not str(e) in support_set else (support_set[str(e)][0]+1, e)
        return {i: v for i, v in support_set.items() if v[0] >= k}


    """
    Compute the support value for a given set of sequences.
    It will return a dictionary with the supports count.
    """
    def support(self, sequences, database) -> dict:
        support_set = dict()
        for s in database:
            for seq in sequences:
                if s.contains(seq):
                    support_set[str(seq)] = (1, seq) if not str(seq) in support_set else (support_set[str(seq)][0]+1, seq)
        return support_set
