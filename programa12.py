'''
Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
al lanzar un dado de seis caras y muestre por pantalla el número en letras 
(dato cadena) de la cara opuesta al resultado obtenido.
* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
1-6, 2-5 y 3-4.
* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
se mostrará el mensaje: "ERROR: número incorrecto.".

'''
#function to translate numbers to letters
def num_a_letra(dado):
        num_a_letra = {
            1: "Uno",
            2: "Dos",
            3: "Tres",
            4: "Cuatro",
            5: "Cinco",
            6: "Seis",
            }
        return num_a_letra.get(dado, "ERROR")
    #Function to show the opposite side 
def lado_opuesto(dado):
        lado_opuesto = {
            1: 6,
            2: 5,
            3: 4,
            4: 3,
            5: 2,
            6: 1,
            }
        return lado_opuesto.get(dado, None)
    
    #main program
dado = int(input("Introduce el resultado del dado: "))
if dado < 1 or dado > 6:
    print("ERROR: número incorrecto.")
else:
       opuesto = lado_opuesto(dado)
       letras = num_a_letra(dado)
print(f"La cara del dado es {letras} y la cara opuesta es {opuesto}.")