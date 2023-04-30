from abc import (ABC, abstractmethod)

class Piece(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def move(self, square):
        pass

    @abstractmethod
    def isValidMove(self, square):
        pass