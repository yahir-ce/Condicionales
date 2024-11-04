'''
Programa que lea una cadena por teclado y compruebe si es un letra mayuscula
Entrada: letra

Salida: "La letra es mayuscula"/"La letra no es mayuscula"
'''

letter = input("Introduce una letra: ")

if letter.isupper() and len(letter) == 1:
    print("La letra es mayuscula")
else:
    print("La letra no es mayuscula")