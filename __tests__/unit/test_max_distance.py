"""Test cases for the max_distance() function."""
# pylint: disable=invalid-name

from math import sqrt
from pytest import approx
from curvereduce import max_distance, perpendicular_distance


def test_1_point():
    """Test max_distance() with one point."""
    points = [(0, 0)]
    distance = max_distance(points)
    assert distance == (0.0, 0)


def test_2_points():
    """Test max_distance() with two points."""
    points = [(0, 0), (1, 1)]
    distance = max_distance(points)
    assert distance == (0.0, 0)


def test_3_points():
    """Test max_distance() with three points."""
    points = [(0, 0), (2, 2), (4, 0)]
    distance = max_distance(points, perpendicular_distance)
    assert distance == (2.0, 1)


def test_4_points():
    """Test max_distance() with four points."""
    points = [(-2, 4), (0, 2), (0, 0), (2, 0)]
    distance = max_distance(points, perpendicular_distance)
    expected_distance = sqrt(2)
    assert distance == (approx(expected_distance), 2)


def test_custom_function():
    """Test max_distance() with custom function."""
    points = [(-2, 4), (0, 2), (0, 0), (2, 0)]
    distance = max_distance(points, lambda p, a, b: 42)
    assert distance == (42, 1)
