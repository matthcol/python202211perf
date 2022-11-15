class Point:
#class Point(object):
    
    def __init__(self, name=None, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.name}({self.x},{self.y})"

