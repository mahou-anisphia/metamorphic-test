import pytest
from assignment2 import split_and_sort


def test_general_input():
    input_array = [5, 2, 9, 8, 3, 7, 4]
    expected_output_even = [2, 4, 8]
    expected_output_odd = [3, 5, 7, 9]
    assert split_and_sort(input_array) == (
        expected_output_odd, expected_output_even)


def test_only_odd_numbers():
    input_array = [1, 3, 5, 7, 9]
    expected_output_even = []
    expected_output_odd = [1, 3, 5, 7, 9]
    assert split_and_sort(input_array) == (
        expected_output_odd, expected_output_even)


def test_only_even_numbers():
    input_array = [2, 4, 6, 8, 10]
    expected_output_even = [2, 4, 6, 8, 10]
    expected_output_odd = []
    assert split_and_sort(input_array) == (
        expected_output_odd, expected_output_even)


def test_input_with_duplicates():
    input_array = [4, 4, 2, 6, 6, 8, 3, 3, 5]
    expected_output_even = [2, 4, 6, 8]
    expected_output_odd = [3, 5]
    assert split_and_sort(input_array) == (
        expected_output_odd, expected_output_even)


def test_all_elements_same():
    input_array = [7, 7, 7, 7, 7]
    expected_output_even = []
    expected_output_odd = [7]
    assert split_and_sort(input_array) == (
        expected_output_odd, expected_output_even)


def test_random_mixed_numbers():
    input_array = [10, 5, 3, 2, 4, 7, 9, 6, 8, 1]
    expected_output_even = [2, 4, 6, 8, 10]
    expected_output_odd = [1, 3, 5, 7, 9]
    assert split_and_sort(input_array) == (
        expected_output_odd, expected_output_even)


def test_general_input_with_duplicates():
    input_array = [5, 2, 9, 8, 3, 7, 4, 5, 2, 9]
    expected_output_even = [2, 4, 8]
    expected_output_odd = [3, 5, 7, 9]
    assert split_and_sort(input_array) == (
        expected_output_odd, expected_output_even)
