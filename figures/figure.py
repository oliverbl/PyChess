
from abc import ABC

import board
from color import Color
from move import Move


class Figure(ABC):

    def __init__(self, x: int, y: int, color: Color, board) -> None:

        self.x = x
        self.y = y
        self.board = board
        self.color = color
        self.beaten = False

    def get_name(self) -> str:
        pass

    def get_value(self) -> int:
        pass

    def get_possible_moves(self) -> list:
        pass

    def set_beaten(self) -> None:
        self.beaten = True

    def is_move_possible(self, new_x: int, new_y: int) -> bool:

        for move in self.get_possible_moves():
            if move.new_x == new_x and move.new_y == new_y:
                return True
        return False

    def __get_possibles_moves_for_directions(self, directions: list) -> list:
        possible_moves = list()

        for dir in directions:
            current_x = self.x + dir[0]
            current_y = self.y + dir[1]
            while 0 <= current_x and current_x < board.Board.NUMBER_OF_COLUMNS and 0 <= current_y and current_y < board.Board.NUMBER_OF_ROWS:
                if self.board.is_position_free(current_x, current_y):
                    possible_moves.append(
                        Move(self, self.x, self.y, current_x, current_y))
                elif self.board.is_opposite_color(current_x, current_y, self.color):
                    possible_moves.append(
                        Move(self, self.x, self.y, current_x, current_y))
                    break
                else:
                    # no move in this direction possible because blocked
                    break
                current_x += dir[0]
                current_y += dir[1]

        return possible_moves

    def get_possible_diagonal_moves(self) -> list:
        return self.__get_possibles_moves_for_directions([(1, 1), (1, -1), (-1, 1), (-1, -1)])

    def get_possible_straight_moves(self) -> list:
        return self.__get_possibles_moves_for_directions([(1, 0), (-1, 0), (0, 1), (0, -1)])

    def get_possible_moves_by_positions(self, positions):
        possible_moves = list()
        for dir in positions:
            new_x = self.x + dir[0]
            new_y = self.y + dir[1]
            if self.board.is_opposite_color(new_x, new_y, self.color) or self.board.is_position_free(new_x, new_y):
                possible_moves.append(self.create_new_move(new_x, new_y))
        return possible_moves

    def create_new_move(self, x: int, y: int) -> Move:
        return Move(self, self.x, self.y, x, y)
