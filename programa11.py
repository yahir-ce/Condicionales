'''
La política de cobro de una compañía telefónica es: cuando se realiza una 
llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
de mañana, 15 %, y en turno de tarde, 10 %. 
Realice un programa para determinar cuánto debe pagar por cada concepto 
una persona que realiza una llamada.

'''
# Función para calcular el costo de la llamada sin impuestos
def calcular_costo_llamada(duracion):
    costo = 0
    if duracion <= 5:
        costo = duracion * 1  
    elif duracion <= 8:
        costo = 5 + (duracion - 5) * 0.80  
    elif duracion <= 10:
        costo = 5 + 3 * 0.80 + (duracion - 8) * 0.70  
    else:
        costo = 5 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50  
    return costo

# Función para calcular el impuesto
def calcular_impuesto(costo, dia, turno=None):
    if dia.lower() == "domingo":
        impuesto = costo * 0.03  
    elif turno.lower() == "mañana":
        impuesto = costo * 0.15  
    else:  
        impuesto = costo * 0.10  
    return impuesto

# Programa principal
def main():
    duracion = int(input("Introduce la duración de la llamada en minutos: "))
    dia = input("Introduce el día de la llamada (domingo u otro): ")

    costo_base = calcular_costo_llamada(duracion)
    print(f"Costo base de la llamada: {costo_base:.2f} euros")

    if dia.lower() != "domingo":
        turno = input("Introduce el turno (mañana/tarde): ")
        impuesto = calcular_impuesto(costo_base, dia, turno)
    else:
        impuesto = calcular_impuesto(costo_base, dia)

    total = costo_base + impuesto
    print(f"Impuesto aplicado: {impuesto:.2f} euros")
    print(f"Total a pagar: {total:.2f} euros")

if __name__ == "__main__":
    main()
