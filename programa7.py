'''
Realize un programa que calcule la potencia, para ello pide por teclado la base
y el exponente. Pueden ocurrir tres cosas:
Si el exponente es positivo solo se imprime la potencia 
Si el exponente es 0, el resultado es 1
Si el exponente es negativo, el resultado es 1/potencia con el exponente positivo
Entrada: base, exponente

Salida: resultado
'''
base = int(input("Introduce el número base: "))
exponente = int(input("Introduce el exponente: "))

if exponente == 0:
    print("El resultado es 1")

elif exponente >= 0:
    print(f"El resultado es {base**exponente}")
    
elif exponente < 0:
    potencia = base ** exponente
    print(f"El resultado es {1/potencia}")