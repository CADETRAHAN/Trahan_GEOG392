import math
from pathlib import Path
print(Path.cwd())

def read_file(file):
    path = r"C:\Users\cadet\DevSource\Trahan_GEOG392\lab\lab03\lab03.txt"
    file = open(path, "r")
    lines =file.readlines()
    file.close
    
    for line in lines:
        components = line.split(",")
        Shape = components[0]

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

#class Circle(Shape):
#    def __init__(self,r):
#        self.r = r
#    def getArea(self):
#        return self.r * self.r * math.pi

#class Triangle(Shape):
#    def __init__(self,l,w):
#        self.l = l
#        self.w = w
#    def getArea(self):
#        return ((self.l * self.w) / 2)

#class Rectangle(Shape):
#    def __init__(self, l, w):
#        self.l = l
#        self.w = w
#    def getArea(self):
#        return self.l * self.w

print(read_file)