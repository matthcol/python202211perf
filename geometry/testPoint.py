# doc pytest: https://docs.pytest.org/en/7.2.x/
# pytest fixture: https://docs.pytest.org/en/7.2.x/how-to/fixtures.html#how-to-fixtures

import pytest
from point import Point

def testEquals():
    p1 = Point()
    p2 = Point()
    assert not (p1 == p2)

def testNotEquals():
    p1 = Point()
    p2 = Point()
    assert p1 != p2

def testEqualsHeterogeneous():
    p1 = Point()
    other = "Toulouse"
    assert not(p1 == other)
    assert not(other == p1)

def testHash():
    p = Point()
    h = hash(p)

def testGt():
    p1 = Point()
    p2 = Point()
    # by default NotImplemented => TypeError
    with pytest.raises(TypeError):
        p1 < p2

@pytest.fixture
def pointA():
    return Point("A", 2, 3)

def testConstructor(pointA):
    assert pointA.name == "A"
    assert pointA.x == 2
    assert pointA.y == 3

def testRepr(pointA):
    assert repr(pointA) == "A(2,3)"

def testStr(pointA):
    assert str(pointA) == "A(2,3)"


