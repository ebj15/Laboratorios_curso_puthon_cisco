# •	Pedir al usuario que ingrese una palabra.
# •	Utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos 
# de cadena y el upper() muy pronto, no te preocupes.
# •	Emplea la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
# •	Asigne las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.
# Analiza el código en el editor. Hemos creado word_without_vowels y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para
#  pedirle a Python que combine las letras seleccionadas en una cadena más larga durante los siguientes giros de bucle, y asignarlo a la variable 
#  word_without_vowels.
# Prueba tu programa con los datos que le proporcionamos.


from ast import Continue
from difflib import HtmlDiff
from multiprocessing import Condition


user_word = input("Ingrese una palabra:")
user_word = user_word.upper()
word_whitout_vouels= ""
# print(user_word)
for i in user_word:
    if i == "A":
        continue
    elif i == "E":
        continue
    elif i == "I":
        continue
    elif i == "O":
        continue
    elif i == "U":
        continue
    else:
        word_whitout_vouels += i
print(word_whitout_vouels)

