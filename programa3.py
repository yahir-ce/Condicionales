'''
Escribe un programa que lea un numero e indique si es par o impar
Enterda: numero
Salida: par/impar
'''
n = int(input("Introduce un numero: "))

if n % 2 == 0:
    print(f"El numero {n} es par")
else:
    print(f"El numero {n} es impar")