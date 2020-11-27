
from .player import Player
import re


class HumanPlayer(Player):

    def __init__(self, *params) -> None:
        super().__init__(*params)


    def validate_input_and_move_if_possible(self, input : str) -> bool:
        input_regex = r'([a-h])([1-8])\s*(?:-> )?\s*([a-h])([1-8])'
        match = re.match(input_regex, input)
        if not match:
            return False
        
        old_x = ord(match.group(1)[0]) - ord('a')
        old_y = int(match.group(2)) -1
        new_x = ord(match.group(3)[0])- ord('a')
        new_y = int(match.group(4)) -1

        return self.board.move(old_x, old_y, new_x, new_y, self.color)