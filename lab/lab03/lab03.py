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


def read_file(file)
