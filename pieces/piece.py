from abc import (ABC, abstractmethod)

class Piece(ABC):

    @abstractmethod
    def name(self):
        '''
        abstract method
        returns the name of the piece
        '''
        pass

    @abstractmethod
    def square(self):
        '''
        abstract method
        returns the current board square that the piece is on
        '''
        pass

    @abstractmethod
    def move(self, square):
        '''
        abstract method
        moves the piece to a new square on the board
        updates current_square to input square if the move is legal
        '''
        pass

    @abstractmethod
    def isValidMove(self, square):
        '''
        abstract method
        returns boolean of whether a move is logically valid
        '''
        pass