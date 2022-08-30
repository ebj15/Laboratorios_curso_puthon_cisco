##Escenario
##La tarea es completar el código para evaluar y mostrar el resultado de
##cuatro operaciones aritméticas básicas.
##El resultado debe ser mostrado en consola.
##Quizá no podrás proteger el código de un usuario que intente dividir entre
##cero. Por ahora, no hay que preocuparse por ello.
##Prueba tu código - ¿Produce los resultados esperados?
##No te mostraremos ningún dato de prueba, eso sería demasiado sencillo.


        ##operaciones matematicas básicas##
print( "**** operaciones matematicas de dos numeros ***")
primer_numero = int(input("Ingresar el primer valor: " ))
segundo_numero = int(input("Ingresar el primer valor: "))
print()

                        ##suma
suma = primer_numero + segundo_numero
print("La suma de:", primer_numero, "mas", segundo_numero, "es igual a:",suma, end="\n"*2)
                        ##resta
resta = primer_numero - segundo_numero
print("La resta de:", primer_numero, "menos", segundo_numero, "es igual a:",resta,end="\n"*2)
                       ##Multiplicación
multiplicacion = primer_numero * segundo_numero
print("La multiplicación de:", primer_numero, "por", segundo_numero, "es igual a:",multiplicacion,end="\n"*2)
                       ##División
division = primer_numero / segundo_numero
print("La división de:", primer_numero, "entre", segundo_numero, "es igual a:",division,end="\n"*2)

print("\n Eso es todo, amigos")
