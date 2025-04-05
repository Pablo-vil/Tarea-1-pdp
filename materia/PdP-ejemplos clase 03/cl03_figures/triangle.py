import math
from figure import Figure


# equilatero
class Triangle(Figure):
    def __init__(self, side: float) -> None:
        self.side: float = side
        
    def area(self) -> float:
        return math.pow(self.side, 2)*math.sqrt(3)/4
    
    def perimeter(self) -> float:
        return 3*self.side
    
    def add(self, fig: "Figure") -> None:
        new_area: float = self.area() + fig.area()
        self.side = math.sqrt(4*new_area/math.sqrt(3))