
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
                
DisplayBoard(board)
EnterMove(board)
DisplayBoard(board)
