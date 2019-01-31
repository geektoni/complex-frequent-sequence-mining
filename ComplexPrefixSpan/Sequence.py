"""
Class which represents the sequence of items which will be stored
in the database
"""
class Sequence():

    def __init__(self, item_list):
        self.sequence = item_list
        self.length = len(self.sequence)
        self.index = 0

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
        if len(otherSequence) > self.length:
            return False

        # Check all the elements
        for i in range(0, len(otherSequence)):
            if not otherSequence[i].compare(self.sequence[i]):
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
    Return an item from the sequence
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
