import math
from pathlib import Path

path = r"C:\Users\cadet\Documents\GitHub\Trahan_GEOG392\lab\lab03\lab03.txt"
file = open(path, "r")

def read_file(file):
    path = r"C:\Users\cadet\Documents\GitHub\Trahan_GEOG392\lab\lab03\lab03.txt"
    file = open(path, "r")
    lines = file.readlines()
    file.close

    for line in lines:
        components = line.strip().split(",")
        Shape = components[0]

    class Triangle(Shape):
        def __init__(self, l, w):
            self.l = l
            self.w = w
        def getArea(self):
            return self.l * self.w / 2

    class Circle(Shape):
        def __init__(self, l):
            self.l = l
        def getArea(self):
            return self.l * self.l * math.pi

    class Rectangle(Shape):
        def __init__(self,l,w):
            self.l = l
            self.w = w
        def getArea(self):
            return self.l * self.w
read_file(file)