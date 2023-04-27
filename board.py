import numpy as np
import chess

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

def showBoard():
    board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
    return board