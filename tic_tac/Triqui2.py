line1 = "+-------+-------+-------+"
line2 = "|       |       |       |"
Lista1= ["|  ",1,"  |"," ",2,"  |","  ",3," |"]
Lista2= ["|  ",5,"  |"," ","X","  |","  ",7," |"]
Lista3= ["|  ",8,"  |"," ",9,"  |","  ",0," |"]
print(line1)
print(line2)
print(*Lista1)
print(line2)
print(line1)
print(line2)
print(*Lista2)
print(line2)
print(line1)
print(line2)
print(*Lista3)
print(line2)
print(line1)

numero =int(input("Ingrese el numero de posición que deseas jugar: "))
if numero == 1:
    Lista = 