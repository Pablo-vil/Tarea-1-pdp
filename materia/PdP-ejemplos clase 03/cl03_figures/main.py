from circle import Circle
from figure import Figure
from rectangle import Rectangle
from triangle import Triangle

figures = [Circle(10), Triangle(6), 
           Rectangle(5, 8)]

for f in figures:
    f.show()

figures[0].add(figures[1])
figures[2].add(figures[1])

for f in figures:
    f.show()