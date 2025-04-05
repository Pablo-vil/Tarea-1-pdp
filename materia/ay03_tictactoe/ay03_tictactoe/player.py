class Player:
    def __init__(self, name: str, symbol: str, color: str) -> None:
        self.name: str = name
        self.symbol: str = symbol
        self.color: str = color

    def get_name(self) -> str:
        return self.name
    
    def get_symbol(self) -> str:
        return self.symbol
    
    def get_color(self) -> str:
        return self.color
    
    def show(self) -> str:
        return f"{self.name}: {self.symbol}"
