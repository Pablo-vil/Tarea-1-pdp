from board_view import BoardView
from board import Board
from player import Player
from rich.console import Console
from rich.text import Text
from rich.prompt import IntPrompt


class Tictactoe:
    def __init__(self, size: int, viewer: BoardView) -> None:
        self.board: Board = Board(size)
        self.players: list[Player] = []
        self.viewer: BoardView = viewer

    def add_player(self, name: str, symbol: str) -> None:
        colors = ["blue", "magenta", "pink", "orange", "gray"]
        self.players.append(Player(name, symbol, colors[(len(self.players))%len(colors)]))

    def start(self) -> None:
        self.show_players()
        self.viewer.display(self.board)
        current_player:int = 0
        winner = None
        while winner is None and self.board.empty_spaces():
            player = self.players[current_player]
            row, col = self.ask_play(player)
            if self.board.play(player, row, col):
                winner = self.board.find_winner()
                self.viewer.display(self.board)
                current_player = (current_player + 1)%len(self.players)
            else:
                self.show_error("Jugada inválida, vuelve a intentarlo")

        console: Console = Console()
        if winner:
            text_winner: Text = Text("El ganador es: ", style="bold green")
            text_winner.append(winner.get_name(), style=f"bold {winner.get_color()}")
            console.print(text_winner)
        else:
            console.print("No hubo ganador")
    
    def show_players(self) -> None:
        console: Console = Console()
        for p in self.players:
            text_player: Text = Text(p.show(), style=p.get_color())
            console.print(text_player)

    def ask_play(self, player: Player) -> tuple[int, int]:
        console: Console = Console()
        text_name: Text = Text("Turno del jugador: ")
        text_name.append(player.get_name(), style=f"bold {player.get_color()}")
        console.print(text_name)
        
        text_instruction: Text = Text("Indica tu jugada ")
        text_instruction.append("fila", style="bold yellow")
        row = IntPrompt.ask(text_instruction)
        text_instruction = Text("Indica tu jugada ")
        text_instruction.append("columna", style="bold yellow")
        col = IntPrompt.ask(text_instruction)

        return row, col
    
    def show_error(self, error_text: str) -> None:
        console: Console = Console()
        text: Text = Text()
        text.append("Error: ", style="bold red")
        text.append(error_text, style="red")
        console.print(text)