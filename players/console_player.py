from .human_player import HumanPlayer

class ConsolePlayer(HumanPlayer):

    def __init__(self, *params) -> None:        
        super().__init__(*params)
    
    def move(self):

        valid_move = False
        while not valid_move:
            print(f"{self.color}: Please enter your move (e.g.: a1 -> h8 or a1 a8)")
            input_string = input()
            valid_move = self.validate_input_and_move_if_possible(input_string)
            if not valid_move:
                print("move was not valid")