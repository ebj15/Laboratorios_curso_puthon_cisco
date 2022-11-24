año = int(input(" Ingresar un año: "))

if año < 1582: print(" Año fuera del calendario gragoriano ")
elif año % 4 != 0:
    print(" Año común ")
elif año % 100 != 0:
    print(" Año bisiesto ")
elif año % 400 != 0:
    print(" Año común ")

else:
    print( " Es un año bisiesto " )
