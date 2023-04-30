from piece import Piece

class Bishop(Piece):

    def __init__(self, color, square):
        self.color = color;
        self.current_square = square;
        self.name = 'Bishop'

    def name(self):
        return self.name
    
    def square(self):
        return self.current_square
    
    def move(self, square):
        pass

    def isValidMove(self, square):
        return False