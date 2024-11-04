'''
Programa que pida dos numeros e indique cual nes el mayor
Si los dos son iguales que muestre el mensaje "Son iguales"

'''
print('Programa que lee dos numeros')
print('Nos dice cual es el mayor')
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
if num1 > num2:
    print(f"El { num1 } es mayor")
else: 
    if num1==num2:
        print(f"Los numeros {num1} y {num2} son iguales")
    else:
        print(f"El {num2} es mayor")
        
