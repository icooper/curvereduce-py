"""Test cases for the simplify_curve() function."""
# pylint: disable=invalid-name,redefined-outer-name

from pytest import fixture, raises
from curvereduce import perpendicular_distance, shortest_distance, simplify_curve


@fixture
def three_points():
    """Fixture for curve of three points."""
    return [(0, 0), (2, 2), (4, 0)]


@fixture
def four_points():
    """Fixture for curve of four points."""
    return [(-2, 4), (0, 2), (0, 0), (2, 0)]


def test_epsilon_subzero():
    """Test simplify_curve() with epsilon < 0."""
    with raises(ValueError, match="Epsilon must not be a negative number."):
        simplify_curve([], -1)


def test_one_point():
    """Test simplify_curve() with a single point."""
    points = [(0, 0)]
    simplified = simplify_curve(points, 1)
    assert simplified == points


def test_two_points():
    """Test simplify_curve() with two points."""
    points = [(0, 0), (1, 1)]
    simplified = simplify_curve(points, 1)
    assert simplified == points


def test_three_points_epsilon_1_shortest_distance(three_points):
    """Test simplify_curve() with 3 points and epsilon = 1 using the shortest
    distance calculation."""
    expected = three_points
    simplified = simplify_curve(three_points, 1, shortest_distance)
    assert simplified == expected


def test_three_points_epsilon_2_shortest_distance(three_points):
    """Test simplify_curve() with 3 points and epsilon = 2 using the shortest
    distance calculation."""
    expected = [three_points[0], three_points[2]]
    simplified = simplify_curve(three_points, 2, shortest_distance)
    assert simplified == expected


def test_four_points_epsilon_05_shortest_distance(four_points):
    """Test simplify_curve() with 4 points and epsilon = 0.5 using the shortest
    distance calculation."""
    expected = four_points
    simplified = simplify_curve(four_points, 0.5, shortest_distance)
    assert simplified == expected


def test_four_points_epsilon_1_shortest_distance(four_points):
    """Test simplify_curve() with 4 points and epsilon = 1 using the shortest
    distance calculation."""
    expected = [four_points[0], four_points[2], four_points[3]]
    simplified = simplify_curve(four_points, 1, shortest_distance)
    assert simplified == expected


def test_four_points_epsilon_2_shortest_distance(four_points):
    """Test simplify_curve() with 4 points and epsilon = 2 using the shortest
    distance calculation."""
    expected = [four_points[0], four_points[3]]
    simplified = simplify_curve(four_points, 2, shortest_distance)
    assert simplified == expected


def test_three_points_epsilon_1_perpendicular_distance(three_points):
    """Test simplify_curve() with 3 points and epsilon = 1 using the
    perpendicular distance calculation."""
    expected = three_points
    simplified = simplify_curve(three_points, 1, perpendicular_distance)
    assert simplified == expected


def test_three_points_epsilon_2_perpendicular_distance(three_points):
    """Test simplify_curve() with 3 points and epsilon = 2 using the
    perpendicular distance calculation."""
    expected = [three_points[0], three_points[2]]
    simplified = simplify_curve(three_points, 2, perpendicular_distance)
    assert simplified == expected


def test_four_points_epsilon_05_perpendicular_distance(four_points):
    """Test simplify_curve() with 4 points and epsilon = 0.5 using the
    perpendicular distance calculation."""
    expected = four_points
    simplified = simplify_curve(four_points, 0.5, perpendicular_distance)
    assert simplified == expected


def test_four_points_epsilon_1_perpendicular_distance(four_points):
    """Test simplify_curve() with 4 points and epsilon = 1 using the
    perpendicular distance calculation."""
    expected = [four_points[0], four_points[2], four_points[3]]
    simplified = simplify_curve(four_points, 1, perpendicular_distance)
    assert simplified == expected


def test_four_points_epsilon_2_perpendicular_distance(four_points):
    """Test simplify_curve() with 4 points and epsilon = 2 using the
    perpendicular distance calculation."""
    expected = [four_points[0], four_points[3]]
    simplified = simplify_curve(four_points, 2, perpendicular_distance)
    assert simplified == expected
