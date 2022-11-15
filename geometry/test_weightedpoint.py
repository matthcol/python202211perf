import pytest
from point import WeightedPoint, Point

@pytest.fixture
def wpointW():
    return WeightedPoint("W", 4, 5, 7.75)


def test_constructor_default():
    wp = WeightedPoint()
    assert wp.name is None
    assert wp.x == 0
    assert wp.y == 0
    assert wp.weight == 0.0

def test_constructor_allArgs(wpointW):
    assert wpointW.name == "W"
    assert wpointW.x == 4
    assert wpointW.y == 5
    assert wpointW.weight == 7.75

def test_fromCoords():
    wp = WeightedPoint.fromCoords(5,7)
    # with classmethod, the return type can be adaptative
    assert type(wp) == WeightedPoint
    assert wp.x == 5
    assert wp.y == 7

def test_pointFromCoords():
    p = WeightedPoint.pointFromCoords(5,7)
    # with staticmethod version, a Point is always returned
    assert type(p) == Point
    assert p.x == 5
    assert p.y == 7

# TODO: check equal, lt, ... are still there with Point definitions
