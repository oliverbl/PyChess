

from .figure import Figure


class Rook(Figure):

    def __init__(self, *params) -> None:
        super().__init__(*params)

    def get_name(self) -> str:
        return 'r'

    def get_value(self) -> int:
        return 5

    def get_possible_moves(self) -> list:
        return self.get_possible_straight_moves()
