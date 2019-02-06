"""
Class which represents the sequence of items which will be stored
in the database
"""
from ComplexPrefixSpan.SequenceItem import SequenceItem


class Sequence():

    def __init__(self, item_list):
        self.sequence = item_list
        self.length = len(self.sequence)
        self.index = 0

    """
    Append an element to the current sequence
    """
    def append(self, item):
        assert isinstance(item, SequenceItem)
        self.sequence.append(item)
        self.length += 1

    """
    Return a copy of the Sequence
    """
    def copy(self):
        return Sequence(self.sequence.copy())

    """
    Return the suffix of this sequence removing its first m elements
    """
    def suffix(self, otherSequence):
        total_suffixes = []
        # Start to scan the list until we find the starting
        # symbol of otherSequence
        suffix_found = False
        for i in range(0, self.length):
            if self.sequence[i].compare(otherSequence[0]):
                suffix_found = True
                # If we found it, check that we have enough
                # space for the otherSequence.
                if self.length-(i+1) < len(otherSequence)-1:
                    return Sequence([])
                # Check that all the successive symbols are
                # actually equals, otherwise return false
                for j in range(0, len(otherSequence)):
                    if not self.sequence[i+j].compare(otherSequence[j]):
                        suffix_found = False
                        break
                if suffix_found:
                    return Sequence(self.sequence[i+len(otherSequence):])
        return Sequence([])

    """
    Check if this sequence contains a given item(s)
    """
    def contains(self, sequenceItems):
        for i in range(0, len(sequenceItems)):
            if not self.sequence[i].compare(sequenceItems[i]):
                return False
        return True

    """
    Check if this sequence starts with the given other sequence
    """
    def starts_with(self, otherSequence) -> bool:

        # If the other sequence is bigger return directly false
        if len(otherSequence) > self.length or len(otherSequence) == 0:
            return False

        # Check all the elements
        for i in range(0, len(otherSequence)):
            if not otherSequence[i].compare(self.sequence[i]):
                return False

        return True

    """
    Check if this contains another sequence
    """
    def __contains__(self, otherSequence) -> bool:

        # If the other sequence is bigger return False
        if self.length < len(otherSequence) or len(otherSequence) == 0:
            return False

        # If they have the same length then do it item by item
        if self.length == len(otherSequence):
            for i in range(0, self.length):
                if not self.sequence[i].compare(otherSequence[i]):
                    return False
            return True

        # Start to scan the list until we find the starting
        # symbol of otherSequence
        status_found = False
        for i in range(0, self.length):
            if self.sequence[i].compare(otherSequence[0]):
                status_found = True
                # If we found it, check that we have enough
                # space for the otherSequence.
                if self.length-(i+1) < len(otherSequence)-1:
                    return False
                # Check that all the successive symbols are
                # actually equals, otherwise return false
                for j in range(1, len(otherSequence)):
                    if not self.sequence[i+j].compare(otherSequence[j]):
                        status_found = False
                        break
                if status_found:
                    return True
        return status_found


    def __eq__(self, other):
        assert(isinstance(other, Sequence))

        if self.length != len(other):
            return False

        for i in range(0, self.length):
            if not self.sequence[i].compare(other[i]):
                return False
        return True

    """
    Remove an item from the sequence
    """
    def __delitem__(self, key):
        del self.sequence[key]

    """
    Get an item from the sequence
    """
    def __getitem__(self, key):
        return self.sequence[key]

    """
    Append an item from the sequence
    """
    def __setitem__(self, key, value):
        self.sequence[key] = value

    """
    Iterator method
    """
    def __iter__(self):
        return self

    """
    Next method used by the iterator
    """
    def __next__(self):
        try:
            result = self.sequence[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    """
    Return the length of this sequence
    """
    def __len__(self):
        return self.length

    """
    Return a string representation of this sequence
    """
    def __str__(self):
        return "".join(list(map(lambda x : str(x), self.sequence)))

    def __repr__(self):
        return "".join(list(map(lambda x: str(x), self.sequence)))

