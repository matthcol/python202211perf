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

@dataclass(eq=False)
class WeightedPoint(Point):

    weight: float = 0.0


@dataclass
class ColoredPoint(Point):

    color: str = 'red'


@dataclass
class WeightedColoredPoint(WeightedPoint, ColoredPoint):
    
    pass


# NB: MRO = Method Resolution Order