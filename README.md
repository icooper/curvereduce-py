# curvereduce

This is an implementation of the [Ramer-Douglas-Peucker curve simplification algorithm](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm) in Python.

[![codecov](https://codecov.io/gh/icooper/curvereduce-py/branch/main/graph/badge.svg?token=YA7H1I6Z4E)](https://codecov.io/gh/icooper/curvereduce-py)

## Usage

Install from the PyPi package repository using `pip install curvereduce`.

```python
from curvereduce import simplify_curve, simplify_curve_to

points = [
    (1.20401E-09, -0.00120428 ),
    (0.018, 0.241799 ),
    (0.1044, 1.34392 ),
    ...
]

# use an explicit epsilon value
simplified_1 = simplify_curve(points, 0.1075)

# or specify a number of points you want to end up with
simplified_2 = simplify_curve_to(points, 20)
```

## License

This work is licensed under the [MIT License](LICENSE).

## Credits

This RDP algorithm implementation is heavily influenced by [Marius Karthaus's JavaScript implementation](https://karthaus.nl/rdp/).
