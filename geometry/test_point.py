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

def test_gt():
    p1 = Point()
    p2 = Point()
    # by default NotImplemented => TypeError
    with pytest.raises(TypeError):
        p1 < p2


def test_constructor(pointA):
    assert pointA.name == "A"
    assert pointA.x == 2
    assert pointA.y == 3

def test_repr(pointA):
    assert repr(pointA) == "A(2,3)"

def test_str(pointA):
    assert str(pointA) == "A(2,3)"


