import math
from pathlib import Path
print(Path.cwd())
path = "C:\Users\cadet\DevSource\Trahan_GEOG392\lab\lab03\lab03.txt"

file = open(path, "r")

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w

class Triangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w / 2

class Circle(Shape):
    def __init__(self, d)
        self.r = r
    def getArea(self):
        return self.r * self.r * math.pi

def read_file(file)
