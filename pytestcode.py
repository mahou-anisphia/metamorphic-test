import pytest
import random
from assignment2 import split_and_sort


def test_division_relationship():
    SI = [3, 2, 2, 5, 6]
    SO_odd, SO_even = split_and_sort(SI)
    FI1 = [SI[0], SI[1], SI[2]]
    FI2 = [SI[3], SI[4]]
    FI1_odd, FI1_even = split_and_sort(FI1)
    FI2_odd, FI2_even = split_and_sort(FI2)
    FI_odd = FI1_odd + FI2_odd
    FI_even = FI1_even + FI2_even
    FO_odd, FO_even = split_and_sort(FI_odd + FI_even)
    assert FO_odd == SO_odd
    assert FO_even == SO_even


def test_k_num_addition_1():
    SI = [4, 4, 2, 6, 6, 8]
    SO_odd, SO_even = split_and_sort(SI)
    K = max(SI) + 1
    FI = SI + [K]
    FO_odd, FO_even = split_and_sort(FI)
    assert FO_even == SO_even
    assert FO_odd == SO_odd + [K]


def test_shuffle():
    SI = [2, 3, 3, 5, 7, 9]
    SO_odd, SO_even = split_and_sort(SI)
    FI = SI[:]
    random.shuffle(FI)
    FO_odd, FO_even = split_and_sort(FI)
    assert FO_even == SO_even
    assert FO_odd == SO_odd


def test_k_addition_relationship():
    SI = [2, 2, 4]
    SO_odd, SO_even = split_and_sort(SI)
    k = 1
    FI = [x + k for x in SI]
    FO_odd, FO_even = split_and_sort(FI)
    FO_odd = [x - k for x in FO_odd]
    FO_even = [x - k for x in FO_even]

    assert FO_odd == SO_even
    assert FO_even == SO_odd


def test_subtraction_relationship():
    SI = [2, 5, 7, 8, 5]
    SO_odd, SO_even = split_and_sort(SI)
    FI = SI[:]
    # Remove the first element of SI (should be 2 in this case)
    FI.remove(SI[0])
    FO_odd, FO_even = split_and_sort(FI)
    assert all(x in SO_even for x in FO_even)
    assert all(x in SO_odd for x in FO_odd)


# def test_addition_of_zero_relationship():
#     SI = [2, 5, 7, 8, 5]
#     SO_odd, SO_even = split_and_sort(SI)
#     FI = SI[:] + [0]
#     error = split_and_sort(FI)
#     assert error == "Error: The number 0 is not a valid input."


if __name__ == "__main__":
    pytest.main()
