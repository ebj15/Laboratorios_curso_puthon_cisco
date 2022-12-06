# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 08:03:45 2022

@author: eduard.buitrago
"""
board =[[1,2,3],["O",'O',"O"],[7,8,9]]
def MakeListOfFreeFields(board):
# La función examina el tablero y construye una lista de todos los cuadros vacíos.
# La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    sing =[]
    for i in range(0,3):
        for j in range(0,3):
            if  (not board[i][j] == "X" and not board[i][j] == "O"):
                Tupla=(i,j)
                sing.append(Tupla)
    return sing    
print(MakeListOfFreeFields(board))

def ganador(board):
    if board[0][0]and board[0][1] and board[0][2] == "X": 
        print("Winner 1 !!! X")
    elif board[1][0]and board[1][1] and board[1][2] == "X": 
        print("Winner 2 !!! X")
    elif board[2][0]and board[2][1] and board[2][2] == "X": 
        print("Winner 3 !!! X")
    elif board[0][0]and board[1][1] and board[2][2] == "X": 
        print("Winner 4 !!! X")
    elif board[2][0]and board[1][1] and board[0][2] == "X": 
        print("Winner 5 !!! X")
    elif board[0][0]and board[0][1] and board[0][2] == "O": 
        print("Winner 1 !!! O")
    elif board[1][0]and board[1][1] and board[1][2] == "O": 
        print("Winner 2 !!! O")
    elif board[2][0]and board[2][1] and board[2][2] == "O": 
        print("Winner 3 !!! O")
    elif board[0][0]and board[1][1] and board[2][2] == "O": 
        print("Winner 4 !!! O")
    elif board[2][0]and board[1][1] and board[0][2] == "O": 
        print("Winner 5 !!! O")

        
ganador(board)