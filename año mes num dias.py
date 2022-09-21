##Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería
##ser universal).
##La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.
##Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LABORATORIO 4.1.3.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de
##la función; este truco acortará significativamente el código.
##Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.
##def is_year_leap(year):
####
year = 0
month = 0
def ingreso_datos():
    global year
    global month
    year = int(input("Ingresa un año: "))

    while year < 1582:
        print(" Año fuera del calendario gregoriano")
        year = int(input("Ingresa un año: "))
    month = int(input("Ingresa un mes en numero: "))
    while month < 1 or month > 12:
        print(" Numero de mes incorrecto")
        month = int(input("Ingresa un mes en numero: "))
ingreso_datos()

 
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

        
print("En el mes ", month, "del año ", year, "hay", days_in_month(year,month), "dias")
     
#
       

#
test_data = [1900, 2000, 2016, 1987,1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600,1600,2400]
test_results = [False, True, True, False, False, False, False, False, False, False, False, False,True,True]
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


