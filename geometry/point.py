from dataclasses import dataclass
from typing import Optional
import math

@dataclass(order=True)
class Point:
    name: Optional[str] = None
    x: int = 0
    y: int = 0

    # p1 - p2 -> distance 
    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.distance(other)

    
    # p += (3,4)
    def __iadd__(self, vector):
        dx, dy = vector
        self.x += dx
        self.y += dy
        return self    

    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    @classmethod
    def fromCoords(cls, x, y):
        return cls(x=x, y=y)

    @staticmethod
    def pointFromCoords(x, y):
        return Point(x=x, y=y)


class WeightedPoint(Point):

    def __init__(self, name=None, x=0, y=0, weight=0.0, **kwargs):
        print("Init WeightedPoint")
        super().__init__(name=name, x=x, y=y, **kwargs)
        self.weight = weight


class ColoredPoint(Point):

    def __init__(self, name=None, x=0, y=0, color='red', **kwargs):
        print("Init ColoredPoint")
        super().__init__(name=name, x=x, y=y, **kwargs)
        self.color = color


class WeightedColoredPoint(WeightedPoint, ColoredPoint):

    def __init__(self, name=None, x=0, y=0, weight=0, color='red', **kwargs):
        print("Init WeigtedColoredPoint")
        # WeightedPoint.__init__(self, name, x, y, weight)
        # ColoredPoint.__init__(self, name, x, y, color)
        super().__init__(name=name, x=x, y=y, weight=weight, color=color, **kwargs)


# NB: MRO = Method Resolution Order