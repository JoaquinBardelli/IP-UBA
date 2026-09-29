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

        
        