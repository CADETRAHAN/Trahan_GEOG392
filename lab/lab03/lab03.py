import math
from pathlib import Path
#global variables
path = r"C:\Users\cadet\Documents\GitHub\Trahan_GEOG392\lab\lab03\lab03.txt"
file = open(path, "r")
#defining main function and reading data
def read_file(file):
    path = r"C:\Users\cadet\Documents\GitHub\Trahan_GEOG392\lab\lab03\lab03.txt"
    file = open(path, "r")
    lines = file.readlines()
    file.close
    #line stripping
    for line in lines:
        components = line.strip().split(",")
        First = components[0]
        Math = []
        #classes with child classes of each shape in the text file
        class Shape:
            def __init__(self, l, w = ""):
                self.l = l
                self.w = w
        class Triangle(Shape):
            def __init__(self, l, w = ""):
                self.l = l
                self.w = w
            def getArea(self):
                Math.append(self.l * self.w / 2)

        class Circle(Shape):
            def __init__(self, l):
                self.l = l
            def getArea(self):
                Math.append(self.l * self.l * math.pi)

        class Rectangle(Shape):
            def __init__(self,l,w = ""):
                self.l = l
                self.w = w
            def getArea(self):
                Math.append(self.l * self.w)
        #if elif statement to use the class of 
        if First == "Triangle":
            Triangle(Shape) 
        elif First == "Circle":
            Circle(Shape)
        elif First == "Rectangle":
            Rectangle(Shape)



    print(Math)
read_file(file)