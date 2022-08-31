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


blocks =2  #int(input("Ingresa el número de bloques: "))

contador = 0 # Cuenta los ciclos del while
suma = 0 # Acumular los niveles hasta completar los bloques disponibles
while contador <= blocks: # Incrementa el valor del contador hasta que sea igual o superior a la cantidad de bloques
    contador += 1
    suma += contador
    if suma >= blocks:
        break # Rompe el ciclo si se alcanzo o sobrepaso el numero de bloques
if suma > blocks: # Si la suma es mayor el ultimo valor de contador se le restara uno para optener la altura
    altura = contador -1
else:
    altura = contador # De lo contrario el valor sera el ultmo que registro el contador  
print("La altura de la piramide es de: ", altura)

   
#print(height)
#	10

#print("La altura de la pirámide:", height)

