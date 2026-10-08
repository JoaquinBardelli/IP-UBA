import random
from queue import LifoQueue as Pila

# ! PARTE 1: Listas

def mostrarPila(pilaOriginal: Pila) -> None:
    res = []
    while not pilaOriginal.empty():
        res.append(pilaOriginal.get())
    print("Pila del ultimo al primer elemento ingresado: ", res)

    for elem in reversed(res):      # del fondo al tope
        pilaOriginal.put(elem)

#1
def generarNrosAlAzar(cantidad:int,desde:int,hasta:int) -> Pila:
    res = Pila()
    for i in range(0,cantidad):
        numeroRandom = random.randint(desde,hasta)
        res.put(numeroRandom)

    return res

#pilaLifo = generarNrosAlAzar(5,0,10)
#mostrarPila(pilaLifo)   
#mostrarPila(pilaLifo)

#2
def cantidadDeElementos(pila:Pila) -> int:
    elementos = []
    cantidad = 0
    while pila.empty() == False:
        elementos.append(pila.get())
        cantidad += 1

    elementos.reverse()
    for elemento in elementos:
        pila.put(elemento)

    return cantidad 

#pila2 = generarNrosAlAzar(5,0,10)
#print(cantidadDeElementos(pila2))
#mostrarPila(pila2)

#3
def buscarElMaximo(pila:Pila) -> int:
    maximo = 0
    elementos = []
    while pila.empty() == False:
        valor = pila.get()
        elementos.append(valor)
        if valor >= maximo:
            maximo = valor

    elementos.reverse()
    for elemento in elementos:
        pila.put(elemento)
    
    return maximo

#pila2 = generarNrosAlAzar(5,0,10)
#print(buscarElMaximo(pila2))
#mostrarPila(pila2)

#4
def buscarNotaMaxima(pila:Pila[(str,int)]) -> tuple[str,int]:
    maximo = ("",0)
    pilaOriginal = []
    while not pila.empty():
        elemento = pila.get()
        pilaOriginal.append(elemento)
        if elemento[1] > maximo[1]:
            maximo = elemento
    for elem in reversed(pilaOriginal):
        pila.put(elem)

    return maximo

"""pila2 = Pila()
pila2.put(("pedro",6))
pila2.put(("pedro2",5))
pila2.put(("pedro3",4))
pila2.put(("pedro4",8))
print(buscarNotaMaxima(pila2))
mostrarPila(pila2)"""

#5
def estaBienBalanceada(caracteres:list[str]) -> bool:
    parentesis = Pila()
    for elem in caracteres:
        if elem == "(":
            parentesis.put(elem)
        elif elem == ")":
            if parentesis.empty():
                return False
            else:
                parentesis.get()

    return parentesis.empty() #* Si esta vacia => esta bien balanceado, si NO esta vacia => sobra algun parentesis

print(estaBienBalanceada(["1",")","+","2","(","(",")"]))