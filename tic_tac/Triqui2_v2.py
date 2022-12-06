from random import randrange
#for i in range(10):
    #print(randrange(8))


#Funcion DisplayBoard: La función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola.
board =[[1,2,3],[4,'X',6],[7,8,9]] # Lista con los valores
freefields =[]
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
            entrada= int(input("Ingresa tu movimiento:"))
        except ValueError: 
            print("Se espera un # entero...")
            continue
        if entrada < 1 or entrada > 9 or entrada == 5:
                print(" ¡Igresa un numero del tablero!")
                continue                        
        else:
            for i in range(0,3):
                for j in range(0,3):
                    if entrada == board[i][j]:
                        board[i][j]= "O"
            return board
                

def MakeListOfFreeFields(board):
# La función examina el tablero y construye una lista de todos los cuadros vacíos.
# La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    for i in range(0,3):
        for j in range(0,3):
            if  (not board[i][j] == "X" and not board[i][j] == "O"):
                Tupla=(i,j)
                freefields.append(Tupla)
                #print(freefields)
    return freefields    

 
def VictoryFor(board):

#     # La función analiza el estatus del tablero para verificar si
#     # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if board[0][0]and board[0][1] and board[0][2] == "X": 
        return print("Winner 1 !!! X")
    elif board[1][0] == board[1][1] == board[1][2] == "X": 
        return print("Winner 2 !!! X")   
    elif board[2][0]== board[2][1] == board[2][2] =="X": 
        return print("Winner 3 !!! X")

    elif board[0][0]== board[1][1] == board[2][2] == "X": 
        return print("Winner 4 !!! X")
    elif board[2][0]== board[1][1] == board[0][2] == "X": 
        return print("Winner 5 !!! X")

    elif board[0][0]== board[1][0] == board[2][0] == "X": 
        return print("Winner 6 !!! X")
    elif board[0][1]== board[1][1] == board[2][1] == "X": 
        return print("Winner 7 !!! X")
    elif board[0][2]== board[1][2] == board[2][2] == "X": 
        return print("Winner 8 !!! X")


    elif board[0][0] == board[0][1] == board[0][2] == "O": 
        return print("Winner 1 !!! O")
    elif board[2][0]== board[2][1] == board[2][2] == "O": 
        return print("Winner 2 !!! O")
    elif board[0][0]== board[1][0] == board[2][0] == "O": 
        return print("Winner 3 !!! O")
    elif board[0][2]== board[1][2] == board[2][2] == "O": 
        return print("Winner 4 !!! O")
    else:
        return False

def DrawMove(board):
    
#     # La función dibuja el movimiento de la máquina y actualiza el tablero.
       
        insertarjugadaen =[]
        jugadadex=(randrange(len(MakeListOfFreeFields(board))-1))
        insertarjugada = list( MakeListOfFreeFields(board)[jugadadex])
        i, j = insertarjugada[0],insertarjugada[1]
        board[i][j] = "X"
    
while VictoryFor(board)== False:
    DisplayBoard(board)
    EnterMove(board)
    MakeListOfFreeFields
    DrawMove(board)
    DisplayBoard(board)
#DrawMove(board)