from piece import Piece

class Knight(Piece):

    def __init__(self, color, square):
        self.color = color;
        self.current_square = square;
        self.name = 'Knight'

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

    #TODO: Edge Case Logic
    def isValidMove(self, square):
        '''
        returns boolean of whether a move is logically valid
        '''
        knight_moves = [17, 15, 10, 6]

        #knights move in an L-shape, up/down 2 and left/right 1 or up/down 1 and left/right 2
        if abs(self.current_square - square) in knight_moves:
            return True

        return False
