import json
import random
from Tile import Tile
from Port import Port

class Board:
    def __init__(self) -> None:
        self.tiles: list[Tile] = []
        self.ports: list[Port] = []

    def load(self, file_path: str) -> None:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for t in data["tiles"]:
                self.tiles.append(Tile(t["id"], t["material"], t["edges"]))
            for p in data["ports"]:
                self.ports.append(Port(p["id"], p["material"]))
    

    

    def random_map(self):

        def random_tile() -> str:
            leters = ["c", "l", "m", "l", "m"]
            numbers = [f"{number:02}" for number in range(1,20)]
            letra = random.choice(leters)
            tipo= random.choice(leters)
            return tipo + letra

        self.tiles.append(Tile(id="d19", material="desierto", edges={"top": random_tile, "top-right": random_tile(), "right": random_tile(), "bottom_right": random_tile(), "bottom": random_tile(), "bottom_left": random_tile(), "left": random_tile(), "top_left": random_tile()}))

        #crear e implementar mapa aleatorio
        pass

    def validate_map(self):

        #validar mapa aleatorio e importado
        pass