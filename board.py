
from functools import reduce
from typing import Final

from color import Color
from figures import bishop, figure, king, knight, pawn, queen, rook
from move import Move

class Board():

    NUMBER_OF_ROWS: Final[int] = 8
    NUMBER_OF_COLUMNS: Final[int] = 8

    def __init__(self) -> None:
        self.board = dict()
        self.figures = dict()
        self.figures[Color.WHITE] = list()
        self.figures[Color.BLACK] = list()
        self.move_history = list()

        self.kings = list()

    def __check_boundaries(self, x: int, y: int) -> bool:
        return (0 <= x and x < Board.NUMBER_OF_COLUMNS) and (0 <= y and y < Board.NUMBER_OF_ROWS)

    def __get_figure_by_position(self, x: int, y: int) -> figure.Figure:
        if not self.__check_boundaries(x, y):
            return None
        key = (x, y)
        if key not in self.board:
            return None
        return self.board[key]

    def is_position_free(self, x: int, y: int) -> bool:
        if not self.__check_boundaries(x, y):
            return False
        key = (x, y)
        if key not in self.board:
            return True
        return self.board[key] == None

    def is_opposite_color(self, x: int, y: int, color: Color) -> bool:
        figure = self.__get_figure_by_position(x, y)
        if figure is None:
            return False
        return figure.color != color

    def move(self, old_x: int, old_y: int, new_x: int, new_y: int, color : Color) -> bool:
        figure = self.__get_figure_by_position(old_x, old_y)
        print(figure)
        if figure is None:
            return False
        
        if figure.color != color:
            return False

        if figure.is_move_possible(new_x, new_y):
            beaten_figure = self.__get_figure_by_position(new_x, new_y)
            if beaten_figure is not None:
                beaten_figure.set_beaten()
            self.board[(old_x, old_y)] = None
            self.board[(new_x, new_y)] = figure
            figure.x = new_x
            figure.y = new_y
            self.move_history.append(Move(figure, old_x, old_y, new_x, new_y))
            return True
        return False

    def is_game_over(self):
        for king in self.kings:
            if king.beaten:
                return True

    def __add_figure(self, figure: figure.Figure):
        self.board[(figure.x, figure.y)] = figure
        self.figures[figure.color].append(figure)

    def __setup_pawns(self):
        for y, color in [(1, Color.WHITE), (Board.NUMBER_OF_COLUMNS - 2, Color.BLACK)]:
            for x in range(0, Board.NUMBER_OF_COLUMNS):
                self.__add_figure(pawn.Pawn(x, y, color, self))

    def __setup_rooks(self):
        for x, y, color in [(0, 0, Color.WHITE), (Board.NUMBER_OF_COLUMNS - 1, 0, Color.WHITE),
                            (0, Board.NUMBER_OF_ROWS - 1, Color.BLACK), (Board.NUMBER_OF_COLUMNS - 1, Board.NUMBER_OF_ROWS - 1, Color.BLACK)]:
            self.__add_figure(rook.Rook(x, y, color, self))

    def __setup_knights(self):
        for x, y, color in [(1, 0, Color.WHITE), (Board.NUMBER_OF_COLUMNS - 2, 0, Color.WHITE),
                            (1, Board.NUMBER_OF_ROWS - 1, Color.BLACK), (Board.NUMBER_OF_COLUMNS - 2, Board.NUMBER_OF_ROWS - 1, Color.BLACK)]:
            self.__add_figure(knight.Knight(x, y, color, self))

    def __setup_bishops(self):
        for x, y, color in [(2, 0, Color.WHITE), (Board.NUMBER_OF_COLUMNS - 3, 0, Color.WHITE),
                            (2, Board.NUMBER_OF_ROWS - 1, Color.BLACK), (Board.NUMBER_OF_COLUMNS - 3, Board.NUMBER_OF_ROWS - 1, Color.BLACK)]:
            self.__add_figure(bishop.Bishop(x, y, color, self))

    def __setup_queens(self):
        for x, y, color in [(3, 0, Color.WHITE), (3, Board.NUMBER_OF_ROWS - 1, Color.BLACK)]:
            self.__add_figure(queen.Queen(x, y, color, self))

    def __setup_kings(self):
        for x, y, color in [(4, 0, Color.WHITE), (4, Board.NUMBER_OF_ROWS - 1, Color.BLACK)]:
            king_figure = king.King(x, y, color, self)
            self.__add_figure(king_figure)
            self.kings.append(king_figure)

    def setup(self):
        self.__setup_pawns()
        self.__setup_rooks()
        self.__setup_knights()
        self.__setup_bishops()
        self.__setup_queens()
        self.__setup_kings()

    def get_fen_string(self):
        rows = []
        for y in range(Board.NUMBER_OF_ROWS -1, -1, -1):
            no_figure_counter = 0
            fen_row = ""
            for x in range(Board.NUMBER_OF_COLUMNS):
                figure = self.__get_figure_by_position(x, y)
                if figure is None:
                    no_figure_counter = no_figure_counter + 1
                else:
                    if no_figure_counter != 0:
                        fen_row += str(no_figure_counter)
                        no_figure_counter = 0
                    name = figure.get_name()
                    name = name.upper() if figure.color == Color.WHITE else name.lower()
                    fen_row += name
            if no_figure_counter != 0:
                fen_row += str(no_figure_counter)
            rows.append(fen_row)
        return '/'.join(rows)

    def get_number_of_possible_moves(self, color : Color):
        figures = self.figures[color]
        possible_moves = 0
        for figure in figures:
            possible_moves = possible_moves + len(figure.get_possible_moves())
        return possible_moves