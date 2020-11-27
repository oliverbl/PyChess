

from .figure import Figure

class Queen(Figure):

    def __init__(self, *params) -> None:
        super().__init__(*params)

    def get_name(self) -> str:
        return 'q'

    def get_value(self) -> int:
        return 9

    def get_possible_moves(self) -> list:
        return self.get_possible_diagonal_moves() + self.get_possible_straight_moves()