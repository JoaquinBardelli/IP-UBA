#! PARTE 4: Programas interactivos usando secuencias

#7.1
def estudiantes()-> list[str]:
    nombres = []
    nombre = input("Ingrese el nombre de su estudiante: ")
    while nombre not in ["listo",""]:
        nombres.append(nombre)
        print("Estudiante ",nombre, " ingresado con exito!")
        nombre = input("Ingrese el nombre de su estudiante: ")
    return nombres

#print(estudiantes())

def historialMonedero() -> list[(str,int)]:
    creditos = 0
    historial = []
    accion = input("Ingrese la opercion a hacer: ")
    while accion != "X":
        if accion == "C":
            monto = int(input("Ingrese el monto a cargar: "))
            historial.append(("C",monto))
            creditos += monto
        elif accion == "D":
            monto = int(input("Ingrese el monto a descontar: "))
            if monto > creditos:
                print("No puede descontar esa cantidad de creditos, ingrese una menor")
            else:
                historial.append(("D",monto))
                creditos -= monto

        accion = input("Ingrese la opercion a hacer: ")
    return historial

#print(historialMonedero())