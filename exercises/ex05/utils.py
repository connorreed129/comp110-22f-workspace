"""EX05- 'list' Utility Functions."""
__author__ = "730478163"


def only_evens(input_list: list[int]) -> list[int]:
    """Given a list of ints, return list of only even numbers."""
    i: int = 0
    evens: list[int] = list()
    while i < len(input_list):
        if input_list[i] % 2 == 0:
            evens.append(input_list[i])
        i += 1
    return evens
        

def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given two lists of ints, return list of the first list followed by the second list."""
    i: int = 0
    combo: list[int] = list()
    while i < len(list_1):
        combo.append(list_1[i])
        i += 1
    i = 0
    while i < len(list_2):
        combo.append(list_2[i])
        i += 1
    return combo


def sub(ints: list[int], start_index: int, end_index: int) -> list[int]:
    """Given an int list, starting index and end index, return subset list of ints and end index -1."""
    a_list: list[int] = list()
    if start_index < 0:
        first_index: int = 0
    else:
        first_index = start_index
    if end_index > len(ints):
        last_index: int = len(ints)
    else:
        last_index = end_index
    if len(ints) == 0 or first_index >= len(ints) or last_index <= 0:
        return a_list
    a_list.append(ints[first_index])
    a_list.append(ints[last_index - 1])
    return a_list
    

    