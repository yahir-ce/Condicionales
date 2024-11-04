'''
Juego Piedra Papel y Tijera
Programa que lea las opciones de 2 jugadores, y muestra el resultado
Empate, gana jugador 1 o gana jugador 2
Si introducimos una opción que no coindica con piedra, papel o tijera
   Diga que opción Incorrecta

'''

player1 = str(input("Jugador 1 introduce tu elección (piedra, papel o tijera): "))
player2 = str(input("Jugador 2 introduce tu elección (piedra, papel o tijera): "))

if player1 == player2:
    print("Empate")
elif player1 == "piedra" and player2 == "tijera":
    print("Gana jugador 1")
elif player1 == "papel" and player2 == "piedra":
    print("Gana jugador 1")
elif player1 == "tijera" and player2 == "papel":
    print("Gana jugador 1")
elif player1 == "tijera" and player2 == "piedra":
    print("Gana jugador 2")
elif player1 == "piedra" and player2 == "papel":
    print("Gana jugador 2")
elif player1 == "papel" and player2 == "tijera":
    print("Gana jugador 2")
else:
    print("Opción incorrecta")

