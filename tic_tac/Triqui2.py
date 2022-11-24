from random import randrange
#for i in range(10):
    #print(randrange(8))


#Funcion DisplayBoard: La función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola.
Lfila1 = [1,2,3]
board =[[1,2,3],[4,'X',6],[7,8,9]] # Lista con los valores
def DisplayBoard(board):    
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print("| ",board[0][0],end="  ")
    print("| ",board[0][1],end="  ")
    print("| ",board[0][2]," |")
    print("|     |     |     |")
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print("| ",board[1][0],end="  ")
    print("| ",board[1][1],end="  ")
    print("| ",board[1][2]," |")
    print("|     |     |     |")
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print("| ",board[2][0],end="  ")
    print("| ",board[2][1],end="  ")
    print("| ",board[2][2]," |")
    print("|     |     |     |")
    print("+-----+-----+-----+")

# #La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
#verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
def EnterMove(board):
    
    while True:  
        try:
            entrada=int(input("Ingresa tu movimiento:"))
        except ValueError: 
            print("Se espera un # entero...")
            continue                        
        else:
            for i in range(0,3):
                for j in range(0,3):
                    if entrada == board[i][j]:
                        board[i][j]= "O"
            return board
                
            
DisplayBoard(board)           
EnterMove(board)

# def MakeListOfFreeFields(board):
#     pass
#     # La función examina el tablero y construye una lista de todos los cuadros vacíos.
#     # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
# def VictoryFor(board, sign):
#     pass
#     # La función analiza el estatus del tablero para verificar si
#     # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
# def DrawMove(board):
#     pass
#     # La función dibuja el movimiento de la máquina y actualiza el tablero.

# def DisplayBoard(board):
#     pass
#     # La función acepta un parámetro el cual contiene el estado actual del tablero
#     # y lo muestra en la consola.

# def EnterMove(board):
#     pass
#     # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
#     # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

# def MakeListOfFreeFields(board):
#     pass
#     # La función examina el tablero y construye una lista de todos los cuadros vacíos.
#     # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.

# def VictoryFor(board, sign):
#     pass
#     # La función analiza el estatus del tablero para verificar si
#     # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

# def DrawMove(board):
#     pass
#     # La función dibuja el movimiento de la máquina y actualiza el tablero.

# DisplayBoard()