"""Test cases for the perpendicular_distance() function."""
# pylint: disable=invalid-name

from math import atan, cos, pi, sqrt
from pytest import approx
from curvereduce import perpendicular_distance


def test_zero_length():
    """Test perpendicular_distance() with a zero-length line."""
    p, a, b = (0, 0), (1, 0), (1, 0)
    distance = perpendicular_distance(p, a, b)
    assert distance == 1


def test_horizontal():
    """Test perpendicular_distance() with a horizontal line."""
    p, a, b = (0, 1), (-1, 0), (1, 0)
    distance = perpendicular_distance(p, a, b)
    assert distance == 1


def test_vertical():
    """Test perpendicular_distance() with a vertical line."""
    p, a, b = (1, 0), (0, -1), (0, 1)
    distance = perpendicular_distance(p, a, b)
    assert distance == 1


def test_45_degrees():
    """Test perpendicular_distance() to a 45-degree line."""
    p, a, b = (0, 0), (2, 0), (0, 2)
    distance = perpendicular_distance(p, a, b)
    expected = sqrt(2)
    assert distance == approx(expected)


def test_sloped():
    """Test perpendicular_distance() to a sloped line."""
    p, a, b = (0, 0), (5, 0), (0, 4.0 / cos(pi / 2.0 - atan(0.75)))
    distance = perpendicular_distance(p, a, b)
    assert distance == approx(4)
