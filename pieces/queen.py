from piece import Piece

class Queen(Piece):

    def __init__(self, color, square):
        self.color = color;
        self.current_square = square;
        self.name = 'Queen'

    def name(self):
        return self.name
    
    def square(self):
        return self.current_square
    
    def move(self, square):
        pass

    def isValidMove(self, square):
        return False
