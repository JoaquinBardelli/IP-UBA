#PARTE 1: Recorrido y busqueda en secuencias
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

print(posSecuenciaOrdenadaMasLarga([1,2,3,1,2,3,4,5,1,1,1,2,3,4]))
