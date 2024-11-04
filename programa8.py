'''
Programa que pida dos números 'nota' y 'edad' y un carácter 'sexo' 
#y muestre el mensaje 'ACEPTADA' si la nota es mayor o igual a cinco, 
#la edad es mayor o igual a dieciocho y el sexo es 'F'. 
#En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. 
#Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.
'''
nota =  int(input("Introduce tu nota: "))
edad = int(input("Introduce tu edad: "))
sexo = input("Introduce tu sexo (F/M): ")

if nota >= 5 and edad >= 18 and sexo == "F":
    print("Aceptado")
elif nota >= 5 and edad >= 18 and sexo == "M":
        print("Posible")
else:
            print("No aceptado")