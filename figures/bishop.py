

from .figure import Figure

class Bishop(Figure):

    def __init__(self, *params) -> None:
        super().__init__(*params)

    def get_name(self) -> str:
        return 'b'

    def get_value(self) -> int:
        return 3

    def get_possible_moves(self) -> list:
        return self.get_possible_diagonal_moves()