# doc pytest: https://docs.pytest.org/en/7.2.x/
# pytest fixture: https://docs.pytest.org/en/7.2.x/how-to/fixtures.html#how-to-fixtures

import pytest
from point import Point

@pytest.fixture
def pointA():
    return Point("A", 2, 3)

@pytest.fixture(params=[
    ("B", 2, 3),
    ("A", 1, 3), 
    ("A", 2, 4)],
    ids = ["name different", "x different", "y different"]
)
def almostPointA(request):
    # pointA with 1 difference
    yield Point(*request.param)
    
def test_equals_heterogeneous():
    p1 = Point()
    other = "Toulouse"
    assert not(p1 == other)
    assert not(other == p1)


def test_equals_defaultPoint():
    p1 = Point()
    p2 = Point()
    assert p1 == p2
    assert p2 == p1

def test_equals_sameContent(pointA):
    pointAbis = Point(pointA.name, pointA.x, pointA.y)
    assert pointA == pointAbis
    assert pointAbis == pointA

def test_equals_differentContent(pointA, almostPointA):
    assert not(pointA == almostPointA)
    assert not(almostPointA == pointA)

def test_notEquals():
    p1 = Point()
    p2 = Point()
    assert not (p1 != p2)
    assert not (p2 != p1) 

def test_hash():
    # with __eq__ redfined, __hash__ is lost
    p = Point()
    with pytest.raises(TypeError):
        hash(p)

# NB: by default NotImplemented => TypeError
# def test_gt():
#     p1 = Point()
#     p2 = Point()
#     with pytest.raises(TypeError):
#         p1 < p2


def test_lt_ok(pointA):
    assert pointA < Point("B")

def test_lt_ko(pointA):
    assert not(pointA < pointA)

def test_gt_ok(pointA):
    assert  Point("B") > pointA

# by default with only __eq__ and __lt__
# TypeError: '<=' not supported between instance
# ok: @total_ordering
def test_le_ok(pointA):
    assert pointA <= Point("B")

# by default with only __eq__ and __lt__
# TypeError: '>=' not supported between instance
# ok: @total_ordering
def test_ge_ok(pointA):
    assert  Point("B") >= pointA




def test_constructor(pointA):
    assert pointA.name == "A"
    assert pointA.x == 2
    assert pointA.y == 3

def test_repr(pointA):
    assert repr(pointA) == "A(2,3)"

def test_str(pointA):
    assert str(pointA) == "A(2,3)"


def test_sub(pointA):
    pointB = Point("B", pointA.x + 4, pointA.y - 3)
    assert (pointA - pointB) == 5
    assert (pointB - pointA) == 5

def test_iadd(pointA):
    pointAref = pointA
    pointA += 4, -7
    # true inplace
    assert pointA is pointAref
    assert pointA.x == 6
    assert pointA.y == -4

def test_iadd_ko(pointA):
    with pytest.raises(ValueError) as excInfo:
        pointA += "Toulouse"
    assert str(excInfo.value) == "too many values to unpack (expected 2)"


def test_fromCoords():
    p = Point.fromCoords(5,7)
    assert type(p) == Point
    assert p.x == 5
    assert p.y == 7

def test_pointFromCoords():
    p = Point.pointFromCoords(5,7)
    assert type(p) == Point
    assert p.x == 5
    assert p.y == 7