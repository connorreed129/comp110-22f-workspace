"""List Utility Functions."""
__author__ = "730478163"


from operator import and_


def all(int_list: list[int], input_int: int) -> bool: 
    """Given a list of ints and an int."""
    i = 0
    if len(int_list) == 0:
        return False
    while i < len(int_list):
        if int_list[i] != input_int:
            return False
        else:
            i += 1
    return True
    

def max(input: list[int]) -> int:
    """Given a list of ints should return largest value."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_value: int = input[0]
    while i < len(input):
        if input[i] > max_value:
            max_value = input[i]
        i += 1
    return max_value
        
                
def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks to see if all ints in a list are equal in value."""
    i: int = 0
    if len(list_1) and len(list_2) == 0:
        return True
    if len(list_1) != len(list_2):
        return False
    else:
        while i < len(list_1) and len(list_2):
            if list_1[i] != list_2[i]:
                return False
            else:
                i += 1
        return True
