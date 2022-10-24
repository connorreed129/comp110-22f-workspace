"""Dictionary Functions."""
__author__ = "730478163"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Given a dict the keys and values of the input should be switched and returned as a dict."""
    inverted: dict[str, str] = {}
    for key in input_dict:
        inverted[input_dict[key]] = key
    if len(inverted) != len(input_dict):
        raise KeyError("Key Error")
    return inverted


def favorite_color(fav_color: dict[str, str]) -> str:
    """Given names (key) and favorite colors (values) determine the favorite color of a list."""
    counting_dict: dict[str, int] = {}
    for color in fav_color:
        if fav_color[color] in counting_dict:
            counting_dict[fav_color[color]] += 1
        else:
            counting_dict[fav_color[color]] = 1
    most_popular_color: int = 0
    return_color: str = ""
    for color in counting_dict:
        if counting_dict[color] > most_popular_color:
            most_popular_color = counting_dict[color]
            return_color = color
    return return_color
    

def count(values: list[str]) -> dict[str, int]:
    """Count the number of times a value appears in a list."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(values):
        if values[i] in result:
            result[values[i]] += 1
        else:
            result[values[i]] = 1
        i += 1
    return result