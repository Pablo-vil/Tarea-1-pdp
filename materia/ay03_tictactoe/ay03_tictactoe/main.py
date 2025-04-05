from board_view import BoardView
from image_board_viewer import ImageBoardView
from console_board_view import ConsoleBoardView
from tictactoe import Tictactoe
from rich.prompt import Prompt, IntPrompt

size: int = IntPrompt.ask("Tamaño del tablero?", default=3)
style: str = Prompt.ask("¿Cómo quieres mostrar el tablero?", choices=['Consola', 'Imagen'], default='Consola')
board_view: BoardView|None = None
if style == 'Consola':
    board_view = ConsoleBoardView()
else:
    board_view = ImageBoardView()

game: Tictactoe = Tictactoe(size, board_view)

count: int = IntPrompt.ask("Cantidad de jugadores?", default=2)
for i in range(count):
    name: str = Prompt.ask(f"Nombre del jugador {i+1}")
    symbol: str = Prompt.ask(f"Símbolo que usará el jugador {name}")
    game.add_player(name, symbol)

game.start()