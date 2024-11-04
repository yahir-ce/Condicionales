'''
Escribe un programa que pida un nombre de usuario y una contraseña, y si se ha introducido "pepe2 y "asdssd" se indica "Has entrado al sistema",
si no se da un error
Enrada: user, password

Salida: Accediste/No accediste al sistema
'''

correct_user: str = "pepe"
correct_password: str = "asdasd"
user = str(input("Introduce el usuario: "))
password = str(input("Introduce la contraseña: "))

if user == correct_user and password == correct_password:
    print("Accediste al sistema")
else:
    print("No accediste al sistema")