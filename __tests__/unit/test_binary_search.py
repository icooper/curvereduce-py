"""Test cases for the binary_search() function."""
# pylint: disable=invalid-name,redefined-outer-name

from pytest import fixture, raises
from curvereduce import binary_search


@fixture
def my_list():
    """Test fixture to provide array."""
    return list(range(0, 10))


def test_found(my_list):
    """Test binary_search() where the result should be found exactly."""

    def test(a):
        return 6 - my_list[a]

    expected = 6
    found = binary_search(test, 0, len(my_list) - 1)
    assert found == expected


def test_close(my_list):
    """Test binary_search() where an exact match is not found, but we get close."""

    def test(a):
        return 5.5 - my_list[a]

    expected = 6
    found = binary_search(test, 0, len(my_list) - 1)
    assert found == expected


def test_bigger(my_list):
    """Test binary_search() where the expected value is larger than the largest
    value in the list."""

    def test(a):
        return 10 - my_list[a]

    expected = max(my_list)
    found = binary_search(test, 0, len(my_list) - 1)
    assert found == expected


def test_smaller(my_list):
    """Test binary_search() where the expected value is smaller than the
    smallest value in the list."""

    def test(a):
        return -1 - my_list[a]

    expected = min(my_list)
    found = binary_search(test, 0, len(my_list) - 1)
    assert found == expected


def test_min_greater_than_max():
    """Test binary_search() where the minimum value is greater than the
    maximum value."""

    with raises(ValueError, match="Minimum value is greater than maximum value."):
        binary_search(lambda x: 0, 10, 0)


def test_min_equal_to_max(my_list):
    """Test binary_search() where the minimum value is equal to the maximum
    value."""

    def test(a):
        return 7.0 - my_list[a]

    expected = 5
    found = binary_search(test, 5, 5)
    assert found == expected
