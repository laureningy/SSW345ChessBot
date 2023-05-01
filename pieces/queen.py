from piece import Piece

class Queen(Piece):

    def __init__(self, color, square):
        self.color = color;
        self.current_square = square;
        self.name = 'Queen'

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
        if self.isValidMove(square):
            self.current_square = square
            return None
        
        return square

    def isValidMove(self, square):
        '''
        returns boolean of whether a move is logically valid
        '''
        
        #Queens can move like rooks and bishops combined
        if abs(self.current_square - square) % 9 == 0 or abs(self.current_square - square) % 7 == 0 or abs(self.current_square - square) % 8 == 0 or abs(self.current_square - square) < 8:
            return True
        
        return False
