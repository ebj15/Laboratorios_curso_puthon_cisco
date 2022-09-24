# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes)
#  y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.
# Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código.
#  Esta prueba es solo el comienzo.

####

year = 0
month = 0
day = 0
def ingreso_datos():
    global year
    global month
    global day
    year = int(input("Ingresa un año: "))

    while year < 1582:
        print(" Año fuera del calendario gregoriano")
        year = int(input("Ingresa un año: "))
    month = int(input("Ingresa un mes en numero: "))
    while month < 1 or month > 12:
        print(" Numero de mes incorrecto")
        month = int(input("Ingresa un mes en numero: "))
    day = int(input("Ingresa un dia en numero: "))
    if days_in_month(year,month) == 28:
         if day < 1 and day > 28:
            print(" Numero de dia incorrecto, el numero de dia debe ser entre 1 y 28:")
            day = int(input("Ingresa un dia en numero: "))
    if days_in_month(year,month) == 29:
         if day < 1 and day > 29:
            print(" Numero de dia incorrecto, el numero de dia debe ser entre 1 y 29:")
            day = int(input("Ingresa un dia en numero: "))
    if days_in_month(year,month) == 30:
         if day < 1 and day > 30:
            print(" Numero de dia incorrecto, el numero de dia debe ser entre 1 y 30:")
            day = int(input("Ingresa un dia en numero: "))
    if days_in_month(year,month) == 31:
         if day < 1 and day > 31:
            print(" Numero de dia incorrecto, el numero de dia debe ser entre 1 y 31:")
            day = int(input("Ingresa un dia en numero: "))
    
    else:
        print(" Numero de dia incorrecto")
        day = int(input("Ingresa un dia en numero: "))
#ingreso_datos()

def is_year_leap(year):
#    
   return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#

#
def days_in_month(year,month):
    
    month_31 = [ 1, 3, 5, 7,8,10,12]
    month_30 = [ 4, 6, 9,11]
    if is_year_leap(year) == True and month == 2:
        return 29
    elif is_year_leap(year) == False and month == 2:
        return 28
    elif month in month_31:
        return 31
    elif month in month_30:
        return 30
    
#
def day_of_year(year, month, day):
    sumadiasxmes = 0
    total_dias = 0
    for i in range(1,month):
        sumadiasxmes += days_in_month(year,i)
    total_dias += sumadiasxmes + day
    print("Año:", year, "Mes:",month,"Dia:", day, "Suma todal de dias a la fecha:", total_dias)
 
    
#
ingreso_datos()
day_of_year(year, month, day)

#
test_data = [1900, 2000, 2016, 1987,1700, ] #1900, 2100, 2200, 2300, 2500, 2600,1600,2400]
test_results = [False, True, True, False, False ]#False, False, False, False, False, False, False,True,True]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
#

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")

