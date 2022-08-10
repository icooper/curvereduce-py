"""Test cases for the simplify_curve_to() function."""
# pylint: disable=invalid-name,redefined-outer-name

from pytest import fixture
from curvereduce import simplify_curve_to


@fixture
def many_points():
    """Fixture for curve of many points."""
    return [
        (1.20401e-09, -0.00120428),
        (0.018, 0.241799),
        (0.1044, 1.34392),
        (0.1494, 1.89758),
        (0.2178, 2.67942),
        (0.5247, 6.91973),
        (1.269, 14.8002),
        (1.6371, 18.0504),
        (2.2104, 22.3001),
        (2.5893, 24.7082),
        (3.1806, 27.6589),
        (3.9924, 30.4127),
        (4.4073, 31.39),
        (5.2713, 32.8131),
        (5.9382, 33.5356),
        (6.8382, 34.1971),
        (7.7517, 34.599),
        (8.6814, 34.8161),
        (9.8613, 34.904),
        (10.4173, 34.8803),
        (11.1417, 34.8032),
        (11.865, 34.6729),
        (12.9515, 34.4192),
        (14.0371, 34.13),
        (14.7603, 33.9307),
        (16.2079, 33.5205),
        (16.9323, 33.3147),
        (18.0181, 33.0196),
        (19.4648, 32.6417),
        (20.1892, 32.453),
        (20.9134, 32.2699),
        (21.6373, 32.0942),
        (22.36, 31.9221),
        (23.0845, 31.7573),
        (24.5326, 31.435),
        (25.2555, 31.2795),
        (25.9798, 31.1348),
        (27.4278, 30.8467),
        (28.8751, 30.5719),
        (30.3234, 30.3101),
        (31.0461, 30.1809),
        (32.1322, 29.9963),
        (33.2184, 29.8226),
        (34.6657, 29.5867),
        (35.7514, 29.4231),
        (36.4754, 29.3182),
        (37.5612, 29.1651),
        (39.3705, 28.9197),
        (40.4564, 28.7797),
        (42.2661, 28.5613),
        (43.7134, 28.3835),
        (45.1612, 28.2194),
        (46.6087, 28.0604),
        (47.3327, 27.9812),
        (48.0567, 27.9055),
        (48.7811, 27.83),
        (50.5904, 27.6477),
        (52.0378, 27.5109),
        (53.1232, 27.4082),
        (54.9332, 27.251),
        (56.0185, 27.1584),
        (57.1038, 27.0701),
        (58.5527, 26.9543),
        (59.6379, 26.8715),
        (60.7239, 26.7892),
        (62.1717, 26.6807),
        (63.2575, 26.6065),
        (64.3433, 26.5366),
        (65.4286, 26.4584),
        (66.1529, 26.4133),
        (66.8761, 26.3701),
        (67.9623, 26.3016),
        (69.0481, 26.2356),
        (69.7714, 26.1927),
        (70.8578, 26.1324),
        (71.5807, 26.0938),
        (73.3904, 25.9954),
        (74.1143, 25.953),
        (74.8387, 25.918),
        (76.286, 25.8486),
        (77.01, 25.8149),
        (77.7343, 25.7787),
        (78.8199, 25.7266),
        (80.6293, 25.6524),
        (82.4392, 25.5782),
        (83.1619, 25.5492),
        (84.9719, 25.4842),
        (86.7816, 25.421),
        (87.5059, 25.3962),
        (88.5912, 25.3638),
        (89.3155, 25.3418),
        (90.0387, 25.3214),
        (91.1249, 25.2914),
        (92.2106, 25.2578),
        (93.2966, 25.2301),
        (94.7432, 25.189),
        (95.8293, 25.1627),
        (96.9156, 25.1362),
        (97.6382, 25.1209),
        (98.3628, 25.1058),
        (99.0872, 25.0926),
        (100.534, 25.0648),
        (101.258, 25.0517),
        (102.344, 25.0337),
        (103.429, 25.0138),
        (104.878, 24.9899),
        (106.688, 24.9631),
        (107.773, 24.9493),
        (108.858, 24.9377),
        (109.583, 24.933),
        (110.306, 24.9261),
        (111.392, 24.9175),
        (112.115, 24.9104),
        (112.84, 24.9088),
        (114.287, 24.8994),
        (115.373, 24.8961),
        (117.183, 24.8923),
        (118.269, 24.8906),
        (119.354, 24.8896),
        (121.164, 24.8829),
        (121.887, 24.8809),
        (122.974, 24.8806),
        (124.421, 24.8773),
        (125.145, 24.8776),
        (125.869, 24.883),
        (127.316, 24.8808),
        (128.764, 24.8861),
        (129.85, 24.8953),
        (130.936, 24.8972),
        (131.659, 24.9034),
        (133.107, 24.9107),
        (133.831, 24.9139),
        (134.916, 24.9186),
        (136.002, 24.9269),
        (137.45, 24.9386),
        (138.173, 24.9428),
        (139.622, 24.9513),
        (141.068, 24.9584),
        (142.517, 24.9644),
        (143.241, 24.9674),
        (143.963, 24.9708),
        (145.05, 24.9757),
        (146.859, 24.9872),
        (147.584, 24.9901),
        (148.308, 24.9883),
        (149.031, 24.9938),
        (149.754, 24.9976),
        (150.479, 25.0018),
        (151.203, 25.0094),
        (151.927, 25.0118),
        (152.65, 25.0161),
        (153.736, 25.0286),
        (155.183, 25.0368),
        (156.269, 25.0525),
        (156.994, 25.0633),
        (157.718, 25.074),
        (160.974, 25.1281),
        (161.698, 25.1416),
        (163.146, 25.1691),
        (163.87, 25.1818),
        (164.594, 25.1939),
        (165.317, 25.2092),
        (166.041, 25.2276),
        (167.489, 25.2626),
        (168.575, 25.2875),
        (169.299, 25.3027),
        (170.022, 25.3221),
        (170.746, 25.3423),
        (171.832, 25.3681),
        (173.28, 25.4073),
        (174.003, 25.4242),
        (175.09, 25.4554),
        (175.812, 25.4752),
        (177.261, 25.5176),
        (177.985, 25.5419),
        (179.432, 25.5877),
        (180.518, 25.6204),
        (182.689, 25.69),
        (183.775, 25.7234),
        (185.222, 25.7738),
        (186.671, 25.8215),
        (188.118, 25.8727),
        (188.842, 25.8953),
        (189.927, 25.9282),
        (190.652, 25.9477),
        (191.375, 25.965),
        (192.461, 25.9954),
        (193.184, 26.0178),
        (194.633, 26.0538),
        (195.718, 26.0786),
        (197.166, 26.1166),
        (197.889, 26.1354),
        (198.975, 26.1596),
        (199.699, 26.1729),
    ]


def test_many_points_to_1_point(many_points):
    """Test simplify_curve_to() with a target of 1 point."""
    expected = [many_points[0], many_points[-1]]
    simplified = simplify_curve_to(many_points, 1)
    assert simplified == expected


def test_many_points_to_20_points(many_points):
    """Test simplify_curve_to() with a target of 20 points."""
    expected_length = 20
    simplified = simplify_curve_to(many_points, 20)
    assert len(simplified) == expected_length


def test_many_points_to_many_points(many_points):
    """Test simplify_curve_to() with a target of 1000 points."""
    expected = many_points
    simplified = simplify_curve_to(many_points, 1000)
    assert simplified == expected
