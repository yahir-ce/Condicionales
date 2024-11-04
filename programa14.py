'''
Escribe un programa que pida un número entero entre uno y doce e imprima el 
número de días que tiene el mes correspondiente.
 Si introducimos otro número nos da un error.

'''
mes = int (input("Introduce un numero del 1 al 12, siendo 1 Enero y 12 Diciembre: "))

if mes < 1 or mes > 12:
    print ("ERROR: el mes no existe")
else:
    match mes:
        case 1:
            print("El mes tiene 31 dias")
        case 2:
            print("El mes tiene 28 dias")
        case 3:
            print("El mes tiene 31 dias")
        case 4:
            print("El mes tiene 30 dias")
        case 5:
            print("El mes tiene 31 dias")
        case 6:
            print("El mes tiene 30 dias")
        case 7:
            print("El mes tiene 31 dias")
        case 8:
            print("El mes tiene 31 dias")
        case 9:
            print("El mes tiene 30 dias")
        case 10:
            print("El mes tiene 31 dias")
        case 11:
            print("El mes tiene 30 dias")
        case 12:
            print("El mes tiene 31 dias")   