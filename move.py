
class Move():   
    def __init__(self, figure, old_x : int, old_y : int, new_x : int, new_y : int) -> None:
        self.figure = figure
        self.new_x = new_x
        self. new_y = new_y
        self.old_x = old_x
        self.old_y = old_y
