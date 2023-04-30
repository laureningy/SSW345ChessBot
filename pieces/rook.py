from piece import Piece

class Rook(Piece):

    def __init__(self, color, square):
        self.color = color;
        self.current_square = square;
        self.name = 'Rook'

    def name(self):
        return self.name
    
    def square(self):
        return self.current_square
    
    def move(self, square):
        pass

    def isValidMove(self, square):
        return False
