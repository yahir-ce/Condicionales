'''
Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
el dí­a correspondiente. 
 Si introducimos otro número nos da un error.

'''
#function to translate numbers to days
def num_a_dia(dia):
    num_a_dia = {
        1: "lunes",
        2: "martes",
        3: "miercoles",
        4: "jueves",
        5: "viernes",
        6: "sabado",
        7: "domingo"
        }
    return num_a_dia.get(dia, None)

#main program
dia = int(input("Introduce el numero del dia de la semana: "))
dia_a_letras = num_a_dia(dia)
if dia < 1 or dia > 7:
    print("ERROR: el dia no existe")
else:
    print(f"El dia de la semana es {dia_a_letras}.")