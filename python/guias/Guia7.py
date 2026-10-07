import math

#!PARTE 1: Recorrido y busqueda en secuencias
#Ejercicio 1
def pertenece1(lista:list[int], numero:int) -> bool:
    for i in range(len(lista)):
        if lista[i] == numero:
            return True
    return False

def pertenece2(lista:list[int], numero:int) -> bool:
    contador = 0
    longitud = len(lista)
    while contador < longitud:
        if lista[contador] == numero:
                    return True
        contador += 1
    return False

def pertenece3(lista:list[int], numero:int) -> bool:
    if numero in lista:
        return True
    else:
        return False
    
#Ejercicio 2
def divideATodos(lista:list[int], numero:int) -> bool:
    for i in range(len(lista)):
        if lista[i] % numero != 0:
            return False
    return True

#Ejercicio 3
def sumaTotal(lista:list[int]) -> int:
    suma = 0
    for num in lista:
        suma += num
    return suma

#Ejercicio 4
def maximo(lista:list[int]) -> int:
    maximo = 0
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

#Ejercicio 5
def minimo(lista:list[int]) -> int:
    minimo = lista[0]
    for num in lista:
        if num < minimo:
            minimo = num
    return minimo

#Ejercicio 6
def ordenados(lista:list[int]) -> bool:
    for num in range(0,len(lista)-1):
        if lista[num] > lista[num + 1]:
            return False
    return True

#Ejercicio 7
def buscarIndice(lista:list[int], valor:int) -> int:
    indice = 0
    for i in range(0,len(lista)):
        if lista[i] == valor:
            indice = i
    return indice

def posMaximo1(lista:list[int]) -> int:
    if len(lista) == 0:
        return -1
    max = maximo(lista)
    return buscarIndice(lista,max)

def posMaximo2(lista:list[int]) -> int:
    maximo = 0
    indice = 0
    if len(lista) == 0:
        return -1
    for i in range (0,len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            indice = i
    return indice

#Ejercicio 8
def posMinimo(lista:list[int]) -> int:
    if len(lista) == 0:
        return -1
    min = minimo(lista)
    return buscarIndice(lista,min)

#Ejercicio 9
def longMayorASiete(palabras:list[str]) -> bool:
    for palabra in palabras:
        if len(palabra) > 7:
            return True
    return False

#Ejercicio 10
def esPalindromo(palabra:str) -> bool:
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    elif palabra == "".join(reverso(palabra)): #!Tambien se podria haber usado list(palabra) == reverso(palabra)
        return True
    return False

def reverso(lista:list) -> list:
    reverso = []
    for i in range(len(lista)-1,-1,-1):
        reverso.append(lista[i])
    return reverso

#Ejercicio 11
def igualesConsecutivos(lista:list[int]) -> bool:
    cantidad = 1
    consecutivos = 1
    if len(lista) < 2:
        return False
    
    for i in range(0,len(lista)-1):
        if lista[i] == lista[i+1]:
            cantidad += 1
        else:
            consecutivos = cantidad
            cantidad = 1

    return consecutivos >= 3

#Ejercicio 12
def vocalesDistintas(palabra:str) -> bool:
    contador = 0
    if 'a' in palabra:
        contador += 1
    if 'e' in palabra:
            contador += 1
    if 'i' in palabra:
            contador += 1
    if 'o' in palabra:
            contador += 1
    if 'u' in palabra:
            contador += 1
    return contador >= 3

def vocalesDistintas2(palabra:str) -> bool:
    vocales = []
    for letra in palabra:
        if letra in "aeiou" and letra not in vocales:
            vocales.append(letra)
    return len(vocales) >= 3

#Ejercicio 13
def posSecuenciaOrdenadaMasLarga(numeros:list[int]) -> int:
    indice = 0
    cantidadConsecutivos = 1
    masLarga = 0
    for i in range(0,len(numeros)-1):
        if numeros[i] < numeros[i+1]:
            cantidadConsecutivos += 1
        else:
            cantidadConsecutivos = 1
        if cantidadConsecutivos > masLarga:   
            masLarga = cantidadConsecutivos
            indice = i - masLarga + 2  #* Aca un +2 porque cantidad de consecutivos se arranca en 1, entonces si estas en la posicion 0, masLarga puede ser =2, y si solo restaramos masLarga el indice nos quedaria negativo
    return indice

#Ejercicio 14
def cantidadDigitosImpares(numeros:list[int]) -> int:
    cantidadImpares = 0
    for numero in numeros:
        cantidadImpares += cantImpares(numero)
    return cantidadImpares


def cantImpares(numero:int) -> int:
    cantidad = 0
    while numero > 0:
        if (numero % 10) % 2 != 0:
            cantidad += 1
        numero = math.floor(numero/10)
    return cantidad


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


#! PARTE 3: Matrices

#5.1
def perteneceACadaUno1(matriz:list[list[int]], num:int, lista:list[bool]):
    for i in range (0,len(matriz)):
        if num in matriz[i]:
            lista[i] = True
        else:
            lista[i] = False

#lista = [True,False,False,True]
#perteneceACadaUno1([[1,2,3],[3,4,5],[7,8,9]],3,lista)
#print(lista)

#5.2
def perteneceACadaUno2(matriz:list[list[int]], num:int, lista:list[bool]):
    lista.clear()
    for i in range (0,len(matriz)):
            if num in matriz[i]:
                lista.append(True)
            else:
                lista.append(False)

#lista = [True,False,False,True]
#perteneceACadaUno2([[1,2,3],[3,4,5],[7,8,9]],3,lista)
#print(lista)

#5.3
def perteneceACadaUno3(matriz:list[list[int]], num:int) -> list[bool]:
    lista = []
    for i in range (0,len(matriz)):
            if num in matriz[i]:
                lista.append(True)
            else:
                lista.append(False)
    return lista

print(perteneceACadaUno3([[1,2,3],[3,4,5],[7,8,9]],3))

#6.1
def esMatriz(matriz:list[list[int]]) -> bool:
    if len(matriz) > 0:
        longitud = len(matriz[0])
        for fila in matriz:
            if len(fila) != longitud:
                return False
    return True

print(esMatriz([[1,2,3],[4,5,6],[7,8,9]]))

#6.2
def filasOrdenadas(matriz:list[list[int]], res:list[bool]):
    res.clear()
    for fila in matriz:
        if ordenados(fila):
            res.append(True)
        else:
            res.append(False)

#6.3
def columna(matriz:list[list[int]], columna:int) -> list[int]:
    res = []
    for fila in matriz:
        res.append(fila[columna])
    return res

print(columna([[1,2,3],[4,5,6],[7,8,9]], 1))  # [2, 5, 8]

#6.4
def columnaOrdenadas(matriz:list[list[int]]) -> list[bool]:
    res =[]
    for i in range(0,len(matriz[0])):
        if ordenados(columna(matriz,i)):
            res.append(True)
        else:
            res.append(False)
    return res

print(columnaOrdenadas([[1,2,3],[4,5,6],[1,8,9]]))  

#6.5
def trasponer(matriz:list[list[int]]) -> list[list[int]]:
    res = []
    for i in range(0,len(matriz)):
        res.append(columna(matriz,i))
    return res

print(trasponer([[1,2,3],[4,5,6],[7,8,9]]))  

#6.6
def quienGanaTateti(tablero:list[list[str]]) -> int:
    res = 2
    for fila in tablero:
        if chequearLista(fila,"X"):
            res = 1
        elif chequearLista(fila, "O"):
            res = 0
    for i in range(0,len(tablero)):
        col = columna(tablero,i)
        if chequearLista(col,"X"):
                    res = 1
        elif chequearLista(col, "O"):
            res = 0
    for diagonal in diagonales(tablero):
        if chequearLista(diagonal,"X"):
            res = 1
        elif chequearLista(diagonal, "O"):
            res = 0
    return res
def chequearLista(lista:list[str], caracter:str) -> bool:
    for elemento in lista:
        if elemento != caracter:
            return False
    return True

def diagonales(tablero:list[list[str]]) -> list[list[str]]:
    res = []
    diagonal1 = []
    diagonal2 = []
    for i in range(0,len(tablero)):
        for j in range(0,len(tablero)):
            if i == j:
                diagonal1.append(tablero[i][j])
    for i in range(0,len(tablero)):
            for j in range(len(tablero)-1,-1,-1):
                if i+j == 2:
                    diagonal2.append(tablero[i][j])
    res.append(diagonal1)
    res.append(diagonal2)
    return res

print(quienGanaTateti([["X","O",""],["","O",""],["X","O",""]]))


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

print(historialMonedero())