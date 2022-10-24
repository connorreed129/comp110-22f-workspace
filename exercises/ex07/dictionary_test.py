"""Tests for EX07- Dictionary Fucntions."""
__author__ = "730478163"

from exercises.ex07.dictionary import invert, count, favorite_color
import pytest


def test_invert_1() -> None:
    """Tests a dictionary with normal result."""
    a: dict[str, str] = {"c": "connor", "k": "kris"}
    assert invert(a) == {"connor": "c", "kris": "k"}


def test_invert_2() -> None:
    """Tests a dictionary with normal result."""
    a: dict[str, str] = {"cat": "tree"}
    assert invert(a) == {"tree": "cat"}


def test_invert_3() -> None:
    """Tests a list of the same word  multiple times."""
    a: dict[str, str] = {"apple": "cat", "a": "c", "b": "tree"}
    assert invert(a) == {"cat": "apple", "c": "a", "tree": "b"}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_favorite_color_1() -> None:
    """Tests a normal dict of people and their favorite colors to see which color is the overall favorite."""
    c: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(c) == "blue"


def test_favorite_color_2() -> None:
    """If there is a tie in favorite color."""
    c: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Connor": "yellow"}
    assert favorite_color(c) == "yellow"


def test_favorite_color_3() -> None:
    """If people all have the same favorite color."""
    c: dict[str, str] = {"Marc": "blue", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(c) == "blue"


def test_count_1() -> None:
    """Tests a list with lots of repeats and indices."""
    c: list[str] = ["connor", "kris", "michael", "connor", "connor"]
    assert count(c) == {"connor": 3, "kris": 1, "michael": 1}


def test_count_2() -> None:
    """Tests a list of same word only."""
    c: list[str] = ["connor", "connor", "connor"]
    assert count(c) == {"connor": 3}


def test_count_3() -> None:
    """Tests a small list."""
    c: list[str] = ["connor", "kris"]
    assert count(c) == {"connor": 1, "kris": 1}