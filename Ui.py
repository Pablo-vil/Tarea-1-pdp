from rich.console import Console, print
from PIL import Image
from Board import Board

class Ui:
    def __init__ (self):
        self.show = Console()

    def Show_board(self, board: Board):
        #Muestra el tablero
        self.print("Hola")