import board
from move import Move
from color import Color
from .figure import Figure
from typing import Final

class Pawn(Figure):

    START_ROW_WHITE : Final = 1
    # START_ROW_BLACK : Final = board.Board.Board.NUMBER_OF_ROWS -1
    START_ROW_BLACK : Final = 6

    def __init__(self, *params) -> None:
        super().__init__(*params)

    def get_name(self) -> str:
        return 'p'
    
    def get_value(self) -> int:
        return 1

    def __is_pawn_at_start(self):
        return (self.y == Pawn.START_ROW_WHITE and self.color == Color.WHITE) or (self.y == Pawn.START_ROW_BLACK and self.color == Color.BLACK)

    def get_possible_moves(self) -> list:

        possible_moves = list()

        direction = 1 if self.color == Color.WHITE else -1

        normal_moves = [direction]
        if self.__is_pawn_at_start():
            normal_moves.append(direction*2)
        
        for move in normal_moves:
            new_y = self.y + move
            if self.board.is_position_free(self.x, new_y):
                possible_moves.append(self.create_new_move(self.x, new_y))

        attacking_moves = [(1, direction), (-1, direction)]
        for move in attacking_moves:
            new_x = self.x + move[0]
            new_y = self.y + move[1]
            if self.board.is_opposite_color(new_x, new_y, self.color):
                possible_moves.append(self.create_new_move(new_x, new_y))
                
        return possible_moves
