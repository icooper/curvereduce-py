"""Library to simplify a 2-dimensional curve using the Ramer-Douglas-Peucker algorithm."""
# pylint: disable=invalid-name

import sys

from math import sqrt
from typing import Callable, List, Tuple

Point = Tuple[float, float]
"""Type representing a generic (x, y) coordinate pair."""

DistanceFunc = Callable[[Point, Point, Point], float]
"""Type representing a distance function."""

DistanceIndex = Tuple[float, int]
"""Type representing the combination of distance and index."""


def perpendicular_distance(p: Point, a: Point, b: Point) -> float:
    """Calculates the perpendicular distance between point `p` and the line
    intersecting points `a` and `b`.

    Args:
        p (Point): point
        a (Point): line point
        b (Point): line point

    Returns:
        float: perpendicular distance
    """

    # horizontal line
    if a[0] == b[0]:
        distance = abs(p[0] - a[0])

    # vertical line
    elif a[1] == b[1]:
        distance = abs(p[1] - a[1])

    # sloped line
    else:
        slope = (b[1] - a[1]) / (b[0] - a[0])
        intercept = a[1] - (slope * a[0])
        distance = abs(slope * p[0] - p[1] + intercept) / sqrt(pow(slope, 2) + 1)

    return distance


def point_distance_squared(i: Point, j: Point) -> float:
    """Calculates the square of the distance between two points

    Args:
        i (Point): point
        j (Point): point

    Returns:
        float: distance squared
    """
    return pow(i[0] - j[0], 2) + pow(i[1] - j[1], 2)


def shortest_distance(p: Point, a: Point, b: Point) -> float:
    """Calculates the shortest distance between point `p` and the line segment
    between points `a` and `b`.

    Args:
        p (Point): point
        a (Point): line point
        b (Point): line point

    Returns:
        float: shortest distance
    """

    line_length_squared = point_distance_squared(a, b)

    # line is actually just a point
    if line_length_squared == 0:
        distance_squared = point_distance_squared(p, a)

    # line is really a line
    else:

        # which endpoint is the point closer to?
        t = (
            (p[0] - a[0]) * (b[0] - a[0]) + (p[1] - a[1]) * (b[1] - a[1])
        ) / line_length_squared

        # point P is closer to point A
        if t < 0:
            distance_squared = point_distance_squared(p, a)

        # point P is closer to point B
        elif t > 1:
            distance_squared = point_distance_squared(p, b)

        # somewhere in the middle
        else:
            distance_squared = point_distance_squared(
                p, (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
            )

    # return the distance
    return sqrt(distance_squared)


# default to the shortest distance function
DEFAULT_DISTANCE_FUNC: DistanceFunc = shortest_distance
"""Default distance calculation function is `shortest_distance()`."""


def max_distance(
    points: List[Point], distance_function: DistanceFunc = DEFAULT_DISTANCE_FUNC
) -> DistanceIndex:
    """Finds the data point in the curve that is furthest away from the
    straight line between the first and last points of the curve.

    Args:
        points (List[Point]): list of points describing the curve
        distance_function (DistanceFunc, optional): function used for
            determining distance. Defaults to DEFAULT_DISTANCE_FUNC.

    Returns:
        DistanceIndex: distance and index of furthest point
    """

    # save the first and last points
    first = points[0]
    last = points[-1]

    # distance and index of furthest point
    distance = -1.0
    index = 0

    # if we have a short list, then we have a shortcut
    if len(points) < 3:
        distance = 0.0
        index = 0

    # loop through the points between the first and the last
    else:
        for i, p in enumerate(points[1:-1]):

            # get the distance using the provided distance function
            d = distance_function(p, first, last)

            # save the distance and index if this is the longest so far
            if d > distance:
                distance = d

                # add 1 since we're off by one due to the `[1:-1]` in the
                # `enumerate()`` function parameter
                index = i + 1

    return distance, index


def binary_search(
    test: Callable[[int], float], minimum: int = 1, maximum: int = sys.maxsize
) -> int:
    """Generic binary search algorithm, used by `simplify_to()`.

    Args:
        test (Callable[[float], float]): Function used to indicate the distance
            between the integer being tested and the target.
        min (int, optional): Low end of the range to test. Defaults to 1.
        max (int, optional): High end of the range to test. Defaults to
            `sys.maxsize`.

    Returns:
        int: the integer closest to the target per `test()`.
    """

    # raise exception if minimum > maxmimum
    if minimum > maximum:
        raise ValueError("Minimum value is greater than maximum value.")

    # set up our initial left, right, and middle points

    l = int(minimum)
    r = int(maximum)
    m = int((l + r) / 2)

    # loop as long as we have something to test
    while r - l >= 1:

        # check the middle point
        t = test(m)

        # it's on target, break out of the loop
        if t == 0:
            break

        # it's low, use the lower half of our search range
        if t < 0:
            r = m - 1

        # it's high, use the upper half of our search range
        else:
            l = m + 1

        # recalculate the middle point
        m = int((l + r) / 2)

    # when we get here, `m` is as close to the target as possible
    return m


def simplify_curve(
    points: List[Point],
    epsilon: float,
    distance_function: DistanceFunc = DEFAULT_DISTANCE_FUNC,
) -> List[Point]:
    """Simplifies a curve with an explicit epsilon value using the
    Ramer-Douglas-Peucker algorithm.

    Args:
        points (List[Point]): points describing the curve
        epsilon (float): minimum distance from the curve
        distance_function (DistanceFunc, optional): Function used for
            determining distance. Defaults to DEFAULT_DISTANCE_FUNC.

    Returns:
        List[Point]: points describing the simplified curve
    """

    # make sure our epsilon value is not negative
    if epsilon < 0:
        raise ValueError("Epsilon must not be a negative number.")

    result: List[Point] = []

    # know when to stop
    if epsilon == 0 or len(points) < 3:
        result = points[:]

    # recursively break down the curve
    else:

        # get the max distance in the curve
        d, i = max_distance(points, distance_function)

        # if the max distance is greater than epsilon
        if d > epsilon:

            # break down the curve at the max distance point and recursively
            # simplify each side
            result = simplify_curve(points[: i + 1], epsilon, distance_function)[
                :-1
            ] + simplify_curve(points[i:], epsilon, distance_function)

        # the max distance is insignificant, so just remove all the points in
        # the middle
        else:
            result = [points[0], points[-1]]

    return result


def simplify_curve_to(
    points: List[Point],
    point_count: int,
    distance_function: DistanceFunc = DEFAULT_DISTANCE_FUNC,
) -> List[Point]:
    """Simplifies a curve to approximately the desired number of data points
    using the Ramer-Douglas-Peucker algorithm. Note that the output may not
    have exactly the desired number of points.

    Args:
        points (List[Point]): points describing the curve
        point_count (int): desired number of points in the simplified curve
        distance_function (DistanceFunc, optional): Function used for
            determining distance. Defaults to DEFAULT_DISTANCE_FUNC.

    Returns:
        List[Point]: points describing the simplified curve
    """

    result: List[Point] = []

    # avoid doing unnecessary work
    if point_count < 3:
        result = [points[0], points[-1]]
    elif point_count >= len(points):
        result = points[:]

    # search for the best epsilon value
    else:

        # figure out a reasonable step size to work with
        step = max_distance(points, distance_function)[0] / sys.maxsize

        # binary search to find a good epsilon value
        result = simplify_curve(
            points,
            step
            * binary_search(
                # return a comparison betwene the target number of points and the
                # number of points generated using the specified epsilon value
                lambda n: len(simplify_curve(points, step * n, distance_function))
                - point_count
            ),
            distance_function,
        )

    return result
