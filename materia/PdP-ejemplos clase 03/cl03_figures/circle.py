import math
from figure import Figure


class Circle(Figure):
    def __init__(self, radius: float) -> None:
        self.radius: float = radius
        
    def area(self) -> float:
        return math.pi*math.pow(self.radius, 2)
    
    def perimeter(self) -> float:
        return 2*math.pi*self.radius
    
    def add(self, fig: "Figure") -> None:
        new_area: float = self.area() + fig.area()
        self.radius = math.sqrt(new_area/math.pi)