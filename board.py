import numpy as np

def createRow():
    row=[]
    for col in range(8):
        row+="-"
    return row

def getGameGrid():
    chessBoard=[]
    for i in range(8):
        chessBoard+=[createRow()]
    return np.matrix(chessBoard)

