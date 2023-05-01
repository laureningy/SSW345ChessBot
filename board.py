import numpy as np

# r n b q k b n r | 57 58 59 60 61 62 63 64
# p p p p p p p p | 49 50 51 52 53 54 55 56
# - - - - - - - - | 41 42 43 44 45 46 47 48 
# - - - - - - - - | 33 34 35 36 37 38 39 40
# - - - - - - - - | 25 26 27 28 29 30 31 32
# - - - - - - - - | 17 18 19 20 21 22 23 24
# P P P P P P P P | 09 10 11 12 13 14 15 16
# R N B Q K B N R | 01 02 03 04 05 06 07 08

def createRow():
    '''Create a row of dashes of length 8, return the row.'''
    row=[]
    for col in range(8):
        row+="-"
    return row

def getGameGrid():
    '''Create 8 rows of dashes, return the 8x8 matrix.'''
    chessBoard=[]
    for i in range(8):
        chessBoard+=[createRow()]
    return np.matrix(chessBoard)