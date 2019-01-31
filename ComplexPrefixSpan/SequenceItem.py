"""
This class represent an item which will present into
the sequences in the database.
"""
class SequenceItem():

    """
    Initialize the object
    """
    def __init__(self):
        pass

    """
    Generate a hash representation of this sequence item.
    This can be used in order to do fast compare.
    """
    def get_hash(self):
        pass

    """
    Method which will be used to compare directly
    two elements of a sequence.
    """
    def compare(self, object) -> bool:
        pass
