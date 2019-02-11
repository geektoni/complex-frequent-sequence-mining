"""
This class represent an item which will present into
the sequences in the database.
"""
class SequenceItem():

    """
    Initialize the object
    """
    def __init__(self, value):
        self.value = value
        pass

    """
    Generate a hash representation of this sequence item.
    This can be used in order to do fast compare.
    """
    def get_hash(self):
        pass

    def __hash__(self):
        return int(self.value.replace(",","").replace("_", "0"))

    """
    Method which will be used to compare directly
    two elements of a sequence.
    """
    def compare(self, object, tresh) -> bool:
        return object.value == self.value

    """
    String representation of this item
    """
    def __str__(self):
        return "{"+str(self.value)+"}"

    def __repr__(self):
        return "{"+str(self.value)+"}"

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value


