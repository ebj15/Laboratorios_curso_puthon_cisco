
##Ejercicio 3
##Crea un programa con un bucle for y una sentencia break.
##El programa debe iterar sobre los caracteres en una dirección de correo
##electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte
##antes de @ en una línea. Usa el esqueleto de abajo:
##
##correo = "edhhu093@gmail.com"
##
##for char in correo:
##    if char == "@":
##        break
##    print(char,end="")

##Ejercicio 4
##Crea un programa con un bucle for y una sentenciacontinue.
##El programa debe iterar sobre una cadena de dígitos,
##reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.
##Usa el esqueleto de abajo:

cadena = "123435045060540506406450"
for num in cadena:
    if num == "0":
       num = "x"
    print(num,end="")
print("#########\n")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
