import random
from queue import LifoQueue as Pila

# ! PARTE 1: Listas

def mostrarPila(pilaOriginal:Pila):
    pila = pilaOriginal
    res = []
    for i in  range(0,pila.qsize()):
        res.append(pila.get())
    print("Pila del ultimo al primer elemento ingresado: ",res)

#1
def generarNrosAlAzar(cantidad:int,desde:int,hasta:int) -> Pila:
    res = Pila()
    for i in range(0,cantidad):
        numeroRandom = random.randint(desde,hasta)
        print(numeroRandom)
        res.put(numeroRandom)

    return res

#pilaLifo = generarNrosAlAzar(5,0,10)
#mostrarPila(pilaLifo)   
#mostrarPila(pilaLifo) #! Mostrar pila saca todos de la pila corregirlo

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

pila2 = generarNrosAlAzar(5,0,10)
print(buscarElMaximo(pila2))
mostrarPila(pila2)