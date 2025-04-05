from figure import Figure


class Rectangle(Figure):
    def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height
        
    def area(self) -> float:
        return self.width*self.height
    
    def perimeter(self) -> float:
        return 2*(self.width + self.height)
    
    def add(self, fig: "Figure") -> None:
        new_area: float = self.area() + fig.area()
        self.width = new_area/self.height