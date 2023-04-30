import numpy as np

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