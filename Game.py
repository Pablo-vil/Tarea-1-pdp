from Board import Board
class Game:
    def __init__(self, players: list):
        self.players = players
        self.turn = 0
        self.board = Board()

