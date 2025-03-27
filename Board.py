import json
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
        #crear e implementar mapa aleatorio
        pass

    def validate_map(self):
        #validar mapa aleatorio e importado
        pass