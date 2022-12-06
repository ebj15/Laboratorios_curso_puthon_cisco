# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:42:25 2022

@author: eduard.buitrago
"""
from random import randrange
board =[[1,2,3],[4,'X','X'],["O","O",9]]
def MakeListOfFreeFields(board):
# La función examina el tablero y construye una lista de todos los cuadros vacíos.
# La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    freefields =[]
    for i in range(0,3):
        for j in range(0,3):
            if  (not board[i][j] == "X" and not board[i][j] == "O"):
                Tupla=(i,j)
                freefields.append(Tupla)
    return freefields 
def MakeListOfFreeFields(board):
    insertarjugadaen =[]
    jugadadex=(randrange(len(MakeListOfFreeFields(board))-1))
    insertarjugada = list( MakeListOfFreeFields(board)[jugadadex])
    i, j = insertarjugada[0],insertarjugada[1]
    board[i][j] = "X"
    
MakeListOfFreeFields()    


 while True:  
        try:
            entrada=int(input("Ingresa tu movimiento:"))
        except ValueError: 
            print("Se espera un # entero...")
            continue
        except:
            if                        
        else:
            for i in range(0,3):
                for j in range(0,3):
                    if entrada == board[i][j]:
                        board[i][j]= "O"
                    else:
                        return
            return board