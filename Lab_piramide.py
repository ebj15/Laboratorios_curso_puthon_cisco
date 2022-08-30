# <!-- Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.
# Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. La pirámide se apila de acuerdo con un principio
# simple: cada capa inferior contiene un bloque más que la capa superior.
# Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede 
# construir utilizando estos bloques.
# Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques y no pueden 
# completar la siguiente capa, terminan su trabajo inmediatamente.
# Prueba tu código con los datos que hemos proporcionado. -->


from re import I
from typing import Counter


blocks = int(input("Ingresa el número de bloques: "))

i = 1
height = 0
counter = 0
while i <= blocks:
    i = i+1
    counter += i+i
    height += 1
    print("Valor temporal de i",i)
    if counter >= blocks:
        break
print(height)
#	10

#print("La altura de la pirámide:", height)

