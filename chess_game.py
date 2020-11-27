
from color import Color
from players.console_player import ConsolePlayer
from players.player import Player
from players import player
from board import Board

import logging
from chess_board_image import get_chess_image

class Chess():
    
    def __init__(self, white_player : Player =  None,
                        black_player  : Player = None) -> None:

        self.board = Board()
        if white_player is None:
            white_player = ConsolePlayer(Color.WHITE, self.board)
        if black_player is None:
            black_player = ConsolePlayer(Color.BLACK, self.board)
        self.players = [white_player, black_player]
        self.board.setup()
        
    def play(self) -> None:

        while not self.board.is_game_over():
            for player in self.players:
                fen_string = self.board.get_fen_string()
                get_chess_image(fen_string)
                logging.log(logging.INFO, fen_string)
                print(f"Number of possible moves: {self.board.get_number_of_possible_moves(player.color)}")
                player.move()



if __name__ == "__main__":

    chess = Chess()
    chess.play()