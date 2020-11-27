
from .figure import Figure

class Knight(Figure):

    def __init__(self, *params) -> None:
        super().__init__(*params)

    def get_name(self):
        return 'n'

    def get_value(self) -> int:
        return 3

    def get_possible_moves(self) -> list:
        directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        return self.get_possible_moves_by_positions(directions)
        
