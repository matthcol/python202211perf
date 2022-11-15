from functools import total_ordering

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
        