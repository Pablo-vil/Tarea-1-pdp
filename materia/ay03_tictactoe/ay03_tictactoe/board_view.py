from abc import ABC, abstractmethod

from board import Board


class BoardView(ABC):

    @abstractmethod
    def display(self, board: Board) -> None:
        ...