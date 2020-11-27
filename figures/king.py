

from color import Color
from .figure import Figure


class King(Figure):

    def __init__(self, *params) -> None:
        super().__init__(*params)

    def get_name(self) -> str:
        return 'k'

    def get_value(self) -> int:
        return 100000

    def get_possible_moves(self) -> list:
        
        directions = [(0, 1), (1, 1), (1,0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        return self.get_possible_moves_by_positions(directions)
        # todo: check for check (mate)

