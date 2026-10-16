from Busqueda import ordenados

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


