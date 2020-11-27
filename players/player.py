from abc import ABC

from color import Color
from board import Board



class Player(ABC):

    def __init__(self, color : Color, board : Board) -> None:
        self.color = color
        self.board = board
        self.resigned = False
        pass

    def move(self):
        pass
