board =[[1,2,3],[4,'X',5],[7,8,9]]
numero= 1


for i in range(0,3):
    for j in range(0,3):
        if numero == board[i][j]:
            board[i][j]= "O"
print(board)

            
    
    

