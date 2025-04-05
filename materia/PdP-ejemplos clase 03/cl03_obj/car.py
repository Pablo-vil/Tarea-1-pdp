class Car:
  def __init__(self, brand: str, year: int) -> None:
    self.brand: str = brand
    self.year: int = year

  def __str__(self) -> str:
    return f'{self.brand} ({self.year})'