##La tarea es preparar un código simple para evaluar o encontrar el tiempo
##final de un periodo de tiempo dado, expresándolo en horas y minutos.
##Las horas van de 0 a 23 y los minutos de 0 a 59. El resultado debe
##ser mostrado en la consola.
##Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos,
##terminará a las 13:16.
##No te preocupes si tu código no es perfecto, está bien si acepta
##una hora invalida, lo más importante es que el código produzca una
##salida correcta acorde a la entrada dada.
##Prueba el código cuidadosamente. Pista: utilizar el operador %
##puede ser clave para el éxito.


hora = 0#int(input("ingrese una hora inicial: "))
minuto = 1#int(input("ingrese minuto inicial: "))
duracion = 2939#int(input("ingrese minutos de duracion: "))
total_min = minuto + duracion
min_to_horas = total_min // 60
#print("minutos to horas",min_to_horas)
hora_final = (hora + min_to_horas) % 24
min_final = total_min % 60

print("Hora final del evento: ",end=(""))
print(hora_final,min_final,sep=(":"))
