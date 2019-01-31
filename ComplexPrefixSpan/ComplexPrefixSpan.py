"""
Class which implements the prefixSpan algorithm to mine
sequential pattern but extender in order to manage sequences
using complex data structures.
"""
class ComplexPrefixSpan:

    def __init__(self):
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
        pass

    """
    Compute the support value for a given sequence
    """
    def support(self, sequence):
        pass
