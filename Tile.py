class Tile:
    def __init__(self, id: str, material: str, edges: dict):
        self.id: str = id
        self.material: str = material
        self.edges: dict[str: str] = edges