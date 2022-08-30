##palabra = input(" ¿ Cual es la palabra secreta? ")
##
##while palabra != "Chupacabra":
##      palabra = input(" ¿ Cual es la palabra secreta? ")
##print( " Otra manera de dejar el bucle sin break")

palabra = input(" ¿ Cual es la palabra secreta? ")

while True:
    palabra = input(" ¿ Cual es la palabra secreta? ")
    if palabra == "Chupacabra":
        break

print( " Saliendo del bucle con Break")
