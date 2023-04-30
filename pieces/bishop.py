from piece import Piece

class Bishop(Piece):

    def __init__(self, color, square):
        self.color = color;
        self.current_square = square;
        self.name = 'Bishop'

    def name(self):
        '''
        returns the name of the piece
        '''
        return self.name
    
    def square(self):
        '''
        returns the current board square that the piece is on
        '''
        return self.current_square
    
    def move(self, square):
        '''
        moves the piece to a new square on the board
        updates current_square to input square if the move is legal
        '''
        pass

    def isValidMove(self, square):
        '''
        returns boolean of whether a move is logically valid
        '''
        return False
