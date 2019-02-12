"""
Class which implements the prefixSpan algorithm to mine
sequential pattern but extender in order to manage sequences
using complex data structures.
"""

import multiprocessing
from itertools import repeat
from ComplexPrefixSpan.Sequence import Sequence
import utils

class ComplexPrefixSpan:

    def __init__(self, database, cores=1, tresh=1):
        self.database=database
        self.cores = cores
        self.tresh = tresh
        pass

    def map_suffix(self, x, suffix):
        return x.suffix(suffix, self.tresh)

    def compute(self, min_support, k, iterative=False):
        if iterative:
            print("[*] Using the iterative version.")
            return self.compute_frequent_complex_patterns_iterative(min_support, k)
        else:
            return self.compute_frequent_complex_patterns_recursive(min_support, k)

    @utils.timing
    def compute_frequent_complex_patterns_iterative(self, min_support, k) -> list:

        frequent_sequences=[]
        frequent_item_list = []
        for i, e in self.one_length_seq_patterns(min_support, self.database).items():
            frequent_item_list.append((Sequence([e[1]]),k))

        while(len(frequent_item_list) != 0):

            e = frequent_item_list.pop(0)

            if (e[1] <=0):
                continue

            projected_database_over_k = self.project_database(e[0], self.database)

            if projected_database_over_k != None:
                frequent_sequences += [e[0]]
                one_frequent = self.one_length_seq_patterns(min_support, projected_database_over_k)
                for i, z in one_frequent.items():
                    tmp = e[0].copy()
                    tmp.append(z[1])
                    frequent_item_list.append((tmp, k-1))
            else:
                continue

        return frequent_sequences

    @utils.timing
    def compute_frequent_complex_patterns_recursive(self, min_support, k) -> list:
        return self._compute_frequent_patterns(min_support, k, self.database, Sequence([]))

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
            return []

        one_frequent = self.one_length_seq_patterns(min_support, database)

        # If the previous frequent item is none, then it means this is the
        # first run of the algorithm. Otherwise, create the new sets of newly
        # frequent items such to do projection.
        frequent_items = []
        if previous_frequent_item == Sequence([]):
            for i, e in one_frequent.items():
                frequent_items.append(Sequence([e[1]]))
        else:
            for i, e in one_frequent.items():
                tmp = previous_frequent_item.copy()
                tmp.append(e[1])
                frequent_items.append(tmp)

        # For each one-frequent patterns, we start mining recursively
        # all the others starting with it
        #counter=0
        for e in frequent_items:

            #print("[*] ({}/{}) Looking for frequent pattern: {}".format(counter+1, len(frequent_items),e))
            #counter += 1

            # Generate the projected database
            projected_database_over_k = self.project_database(e, self.database)

            # This means that the "frequent sequence" we are looking at
            # actually does not exists inside the database, therefore we will
            # not add it to the list of frequent sequence
            if projected_database_over_k != None:
                frequent_sequences += [e]
            else:
                continue

            result = self._compute_frequent_patterns(min_support, k-1, projected_database_over_k, e)
            frequent_sequences += result
        return frequent_sequences

    """
    Returns the projected database for a given suffix.
    """
    def project_database(self, suffix, database) -> list:

        # Consider only the sequences which have the suffix inside them
        result = list(filter(lambda x: suffix in x, database))

        # If the list is empty, this means that the suffix does
        # not exists inside the database
        if len(result) == 0:
            return None

        # Return the projected database over the suffix
        with multiprocessing.Pool(self.cores) as pool:
            return list(pool.starmap(self.map_suffix, zip(result, repeat(suffix))))

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
                if s.contains(seq, self.tresh):
                    support_set[str(seq)] = (1, seq) if not str(seq) in support_set else (support_set[str(seq)][0]+1, seq)
        return support_set
