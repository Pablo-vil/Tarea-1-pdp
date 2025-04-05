from person import Person


class Worker(Person):
    def __init__(self, name: str, company: str) -> None:
        super().__init__(name)
        self.company: str = company

    def get_company(self) -> str:
        return self.company
    
    def change_company(self, new_company: str) -> None:
        self.company = new_company

    def greet(self) -> str:
        return super().greet() + f', trabajo en {self.company}'