class Person:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def get_name(self) -> str:
        return self.name
        
    def greet(self) -> str:
        return f'Soy persona y me llamo {self.name}'
    
    def __str__(self) -> str:
        return self.greet()