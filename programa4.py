'''
Crea un programa que pida al usuario dos numeros y muestre su division, si el segundo
no es 0, o un mensaje de aviso en caso contrario
Entrada: n1, n2

Salida: division/advertencia si el segundo numero es 0
'''

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

if numero2 == 0:
    print("No se puede realizar una division entre 0")
else:
    print(f"El resultado de la division es {numero1/numero2}")