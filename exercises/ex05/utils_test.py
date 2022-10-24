"""Tests for EX05- 'list' Utility Functions."""
__author__ = "730478163"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens1() -> None:
    """Test for only evens 1."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(test_list) == [2, 4]


def test_only_evens2() -> None:
    """Test for only evens 2."""
    test_list: list[int] = [1, 3, 5]
    assert only_evens(test_list) == []


def test_only_evens3() -> None:
    """Test for only evens 3."""
    test_list: list[int] = [2, 2, 2]
    assert only_evens(test_list) == [2, 2, 2]


def test_concat1() -> None:
    """Test for concat 1."""
    test_list_1: list[int] = [1, 2, 3]
    test_list_2: list[int] = [4, 5, 6]
    assert concat(test_list_1, test_list_2) == [1, 2, 3, 4, 5, 6]


def test_concat2() -> None:
    """Test for concat 2."""
    test_list_1: list[int] = [1, 7, 9]
    test_list_2: list[int] = [4, 5, 6]
    assert concat(test_list_1, test_list_2) == [1, 7, 9, 4, 5, 6]


def test_concat3() -> None:
    """Test for concat 3."""
    test_list_1: list[int] = [1, 2, 3]
    test_list_2: list[int] = []
    assert concat(test_list_1, test_list_2) == [1, 2, 3]


def test_sub1() -> None:
    """Test for sub 1."""
    input_list: list[int] = [2, 1, 4, 3, 5]
    start_index: int = 1
    end_index: int = 4
    assert sub(input_list, start_index, end_index) == [1, 3]


def test_sub2() -> None:
    """Test for sub 2."""
    input_list: list[int] = [10, 20, 30, 40]
    start_index: int = 1
    end_index: int = 3
    assert sub(input_list, start_index, end_index) == [20, 30]


def test_sub3() -> None:
    """Test for sub 3."""
    input_list: list[int] = [2, 2, 2, 2, 2, 2, 2]
    start_index: int = 1
    end_index: int = 5 
    assert sub(input_list, start_index, end_index) == [2, 2]