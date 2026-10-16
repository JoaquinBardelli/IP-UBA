from Busqueda import sumaTotal

#! PARTE 2: Recorrido filtrando, modificando y procesando secuencias
#Ejercicio 1
def cerosEnPosicionesPares(lista:list[int]):
    for i in range(0,len(lista)):
        if i % 2 == 0:
            lista[i] = 0

#Ejercicio 2
def cerosEnPosicionesPares2(lista:list[int]) -> list[int]:
    lista2 = lista.copy()
    for i in range(0,len(lista2)):
        if i % 2 == 0:
            lista2[i] = 0
    return lista2

#Ejercicio 3
def sinVocales(palabra:str) -> str:
    palabra2 = []
    for letra in palabra:
        if letra not in "aeiouAEIOU":
            palabra2.append(letra) #! podria crear una variable res = "" y hacer res += letra
    return palabra2 #*Esto devuelve una lista de caracteres, si queremos devolver un string todo junto hay que hacer "".join(palabra2)

#Ejercicio 4
def reemplazaVocales(palabra:str) -> str:
    res = ""
    for i in range(0,len(palabra)):
        if palabra[i] not in "aeiouAEIOU":
            res += palabra[i]
        else:
            res += '_'
    return res

#Ejercicio 5
def daVueltaStr(palabra:str) -> str:
    palabra2 = list(palabra)
    palabra2.reverse()
    return palabra2

def daVueltaStr2(palabra:str) -> str:
    res = "" 
    for i in range (len(palabra)-1,-1,-1):  #! Tambien se podria hacer recorriendo de adelante para atras y hacer res = letra + res
        res += palabra[i]
    return res

#Ejercicio 6
def eliminarRepetidos(palabra:str) -> str:
    res = ""
    for letra in palabra:
        if letra not in res:
            res += letra
    return res

#EJERCICIO 3
def resultadoMateria(notas:list[int]) -> int:
    promedio = sumaTotal(notas)/len(notas)
    for num in notas:
        if num < 4:
            return 3
    if promedio < 4:
        return 3
    elif 4 <= promedio < 7:
        return 2

    return 1    

#EJERCICIO 4
def saldoActual(movimientos: list[(str,int)]) -> int:
    saldo = 0
    for movimiento in movimientos:
        if movimiento[0] == 'I':
            saldo += movimiento[1]
        elif movimiento[0] == 'R':
            saldo -= movimiento[1]
        else:
            print("Ingreso una operacion invalida")
    return saldo


