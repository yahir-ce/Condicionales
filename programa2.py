'''
Programa que pida un numero y diga si es positivo, negativo o 0
Entrada: numero
Salida: positivo/negativo/0
'''
numero = int(input("Introduce un numero: "))

if numero > 0:
    print(f"El numero {numero} es positivo")
elif numero < 0:
    print(f"El numero {numero} es negativo")
elif numero == 0:
    print(f"El numero {numero} es 0")