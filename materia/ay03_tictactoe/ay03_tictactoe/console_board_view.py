from board import Board
from board_view import BoardView
from rich.console import Console
from rich.text import Text


class ConsoleBoardView(BoardView):

    def display(self, board: Board) -> None:
        console: Console = Console()
        size = board.size()
        for row in range(size):
            text_row: Text = Text()
            for col in range(size):
                cell = board.cell_state(row, col)
                if cell is None:
                    text_row.append("  | ")
                else:
                    text_row.append(f"{cell.get_symbol()} | ", style=cell.get_color())
            console.print(text_row)