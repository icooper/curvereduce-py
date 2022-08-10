"""Test cases for the point_distance_squared() function."""
# pylint: disable=invalid-name,redefined-outer-name

from curvereduce import point_distance_squared


def test_same_point():
    """Tests point_distance_squared() with the same point."""
    point = (0, 0)
    expected = 0
    distance_squared = point_distance_squared(point, point)
    assert distance_squared == expected


def test_horizontal():
    """Tests point_distance_squared() with two points on the same horizontal
    line."""
    i, j = (-1, 0), (1, 0)
    expected = 4
    distance_squared = point_distance_squared(i, j)
    assert distance_squared == expected


def test_vertical():
    """Tests point_distance_squared() with two points on the same vertical
    line."""
    i, j = (0, 1), (0, -1)
    expected = 4
    distance_squared = point_distance_squared(i, j)
    assert distance_squared == expected


def test_45_degrees():
    """Tests point_distance_squared() with two points on a 45-degree angle."""
    i, j = (1, 1), (-1, -1)
    expected = 8
    distance_squared = point_distance_squared(i, j)
    assert distance_squared == expected
