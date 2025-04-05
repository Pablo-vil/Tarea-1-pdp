from player import Player
from rich.console import Console
from rich.text import Text


class Board:
    def __init__(self, size: int) -> None:
        self.board: list[list[Player|None]] = [[None for _ in range(size)] for _ in range(size)]

    def play(self, player: Player, row: int, col: int) -> bool:
        if 0 <= row < self.size() and 0 <= col < self.size() and self.board[row][col] is None:
            self.board[row][col] = player
            return True
        return False
    
    def find_winner(self) -> Player|None:
        size = len(self.board)
        for i in range(size):
            for j in range(size):
                player = self.board[i][j]
                if player is None:
                    continue  # Solo buscamos secuencias iniciadas por un jugador
                
                # Comprobar 3 en línea horizontal (si hay suficiente espacio a la derecha)
                if j <= size - 3:
                    if self.board[i][j+1] == player and self.board[i][j+2] == player:
                        return player
                
                # Comprobar 3 en línea vertical (si hay suficiente espacio abajo)
                if i <= size - 3:
                    if self.board[i+1][j] == player and self.board[i+2][j] == player:
                        return player
                
                # Comprobar diagonal (de arriba a la izquierda hacia abajo a la derecha)
                if i <= size - 3 and j <= size - 3:
                    if self.board[i+1][j+1] == player and self.board[i+2][j+2] == player:
                        return player
                
                # Comprobar diagonal inversa (de arriba a la derecha hacia abajo a la izquierda)
                if i <= size - 3 and j >= 2:
                    if self.board[i+1][j-1] == player and self.board[i+2][j-2] == player:
                        return player
        
        # Si no se encontró secuencia ganadora, retornamos None
        return None
    
    def empty_spaces(self) -> bool:
        return len([1 for r in self.board if len([c for c in r if c is None]) > 0]) > 0
    
    ##############
    # Agregamos métodos para obtener la información del tablero

    def size(self) -> int:
        return len(self.board)
    
    def cell_state(self, row: int, col: int) -> Player|None:
        return self.board[row][col]
