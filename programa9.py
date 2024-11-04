'''
Programa que pida tres números y los muestre ordenados (de mayor a menor);

Entrada: n1, n2, n3
Salida, de mayor a menor: n1, n2, n3

'''
n1 = int(input("Introduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))
n3 = int(input("Introduce el tercer numero: "))

# Crear una lista con los tres números
numeros = [n1, n2, n3]

# Ordenar los números de mayor a menor
numeros_ordenados = sorted(numeros, reverse=True)

# Mostrar los números ordenados
print("Números de mayor a menor:", numeros_ordenados)
