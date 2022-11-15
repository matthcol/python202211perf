from functools import total_ordering
import math

@total_ordering
class Point:
#class Point(object):
    
    def __init__(self, name=None, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.name}({self.x},{self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.name, self.x, self.y) \
            == (other.name, other.x, other.y)


    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.name, self.x, self.y) \
            < (other.name, other.x, other.y)


    # p1 - p2 -> distance 
    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return math.hypot(self.x - other.x, self.y - other.y)

    
    # p += (3,4)
    def __iadd__(self, vector):
        dx, dy = vector
        self.x += dx
        self.y += dy
        return self
    