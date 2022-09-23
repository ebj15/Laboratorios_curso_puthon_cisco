

year =2000
month = 12
day = 3
#if day < 1 or day > 31 or year != int() or month < 1 or month > 12:
    #return 

#*****************************+++++++++++++++++******************************    
def is_year_leap(year):#
    if year < 1582:# Limite del calendario Gregoriano
        return "Año fuera del calendario Gregoriano"
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    if year % 400 != 0:
       return False
    else:
       return True #En cualquier otro caso es bisiesto.

print(is_year_leap(year))# Llamado de la función
#*******************************+++++++++++++++++*****************************
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
  	yr = test_data[i]
  	print(yr,"->",end="")
  	result = is_year_leap(yr)
  	if result == test_results[i]:
  		print("OK")
  	else:
  		print("Fallido")

#*******************************+++++++++++++++********************************
def days_in_month(year, month): 
    mes30 = [4,6,9,11] 
    mes31 = [1,3,5,7,8,10,12]
    dias = [28,29,30,31]
    for i in range(len(mes30)):
        m30=mes30[i]
        if m30==month:
            return(dias[2])          
    for i in range(len(mes31)):
        m31=mes31[i]
        if m31==month:
           return(dias[3])            
# Aqui se analiza si es febrero       
    if is_year_leap(year) == True and month == 2:       
       return(dias[1])      
    if is_year_leap(year) == False and month == 2:       
        return(dias[0])
    
print(days_in_month(year, month))
#********************************+++++++++++++++*******************************
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end=" ")
	result = days_in_month(yr, mo)
     
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
print("Año:", year, "Mes: ",month)
#*****************************++++++++++++++++*********************************
def day_of_year(year, month, day):        
    print("Año:", year, "Mes: ",month, "Dia: ",day)
    diasbisiesto= [31,29,31,30,31,30,31,31,30,31,30,31]
    dias_no_bis= [31,28,31,30,31,30,31,31,30,31,30,31]
    total = 0
    month_to_day = 0
    day_in_year = 0
    #SI el año es bisisiesto y mes diferente de enero
    if is_year_leap(year) == True and month > 1:
        total=diasbisiesto[:(month-1)]
        for total in total:            
            month_to_day  += total
            print("Montoday",month_to_day)
            print("Totooo",total)
            day_in_year = month_to_day + day 
        return day_in_year
    if is_year_leap(year) == True and month == 1:# Si es enero de un bisiesto
        print("Test")
        return day
   # Si el año no es bisiesto y mes diferente de enero
    if is_year_leap(year) == False and month > 1:
        total=dias_no_bis[:(month-1)]
        for total in total:
            month_to_day  += total
            print("Año Falso",month_to_day)
            print("Año falso",total)
            day_in_year = month_to_day + day 
        return day_in_year
    if is_year_leap(year) == False and month == 1: #Si es enero de no bisiesto
                return day
    else:
                return ("Error de datos", None)
               
print(day_of_year(year, month, day))         
# =============================================================================