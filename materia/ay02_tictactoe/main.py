from tictactoe import Tictactoe
from rich.prompt import Prompt, IntPrompt

size: int = IntPrompt.ask("Tamaño del tablero?", default=3)
game: Tictactoe = Tictactoe(size)

count: int = IntPrompt.ask("Cantidad de jugadores?", default=2)
for i in range(count):
    name: str = Prompt.ask(f"Nombre del jugador {i+1}")
    symbol: str = Prompt.ask(f"Símbolo que usará el jugador {name}")
    game.add_player(name, symbol)

game.start()