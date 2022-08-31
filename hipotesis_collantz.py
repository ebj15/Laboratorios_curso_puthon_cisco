# En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:
# 1.	Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
# 2.	Si es par, evalúa un nuevo c0 como c0 Ã· 2.
# 3.	De lo contrario, si es impar, evalúe un nuevo  c0  como 3 Ã c0 + 1.
# 4.	Si c0 â  1, salta al punto 2.
# La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.
# Por supuesto, es una tarea extremadamente compleja usar una computadora para probar la hipótesis de cualquier número natural (incluso puede requerir inteligencia artificial), pero puede usar Python para verificar algunos números individuales. Tal vez incluso encuentres el que refutaría la hipótesis.
# Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1. También queremos que cuente los pasos necesarios para lograr el objetivo. Tu código también debe mostrar todos los valores intermedios de c0.
# Sugerencia: la parte más importante del problema es como transformar la idea de Collatz en un bucle while- esta es la clave del éxito.
# Prueba tu código con los datos que hemos proporcionado.


entero =40  #int(input("Ingresa un valor entero positivo diferente de cero: "))
while entero <= 0:
    print("Debe ser un entero positivo diferente de cero")
    entero = int(input("Ingresa un valor entero positivo diferente de cero: "))
c0 = entero
while c0 % 2 == 0:
    c0 /= 2
    print(c0)
    if c0 % 2 != 0:
        c0 = (c0 *3) + 1
        print(c0)
    else:
        if c0 == 1.0:
            break

print(c0)