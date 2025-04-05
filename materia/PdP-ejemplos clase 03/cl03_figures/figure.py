from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        ...
     
    @abstractmethod
    def perimeter(self) -> float:
        ...

    @abstractmethod
    def add(self, fig: "Figure") -> None:
        ...
        
    def show(self) -> None:
        print(f'La figura tiene area {self.area()} y perimetro {self.perimeter()}')