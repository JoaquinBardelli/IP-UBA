import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

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
def buscarElMaximo(pila:Pila[int]) -> int:
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

#print(estaBienBalanceada(["1",")","+","2","(","(",")"]))

#6
def evaluarExpresion1(expresion:str) -> float:
    operandos = Pila()
    numero = ""
    for caracter in expresion:
        if caracter != " ":
            if caracter not in "+-*/":     #! Esta version funciona bien pero no admite numeros negativos
                numero += caracter
            else:
                ultimo = operandos.get()
                primero = operandos.get()
                match caracter:
                    case '+':
                        operandos.put(ultimo + primero)
                    case '*':
                        operandos.put(ultimo*primero)
                    case '-':
                        operandos.put(primero-ultimo)
                    case '/':
                        operandos.put(primero/ultimo)
        elif numero != "":
            operandos.put(int(numero))
            numero = ""

    return operandos.get()


def evaluarExpresion2(expresion:str) -> float:
    numeros = Pila()
    for elemento in expresion.split():  #! .split() separa un str en elementos de una lista cada vez que hay un espacio
        if elemento in "+-*/":
            ultimo = numeros.get()
            primero = numeros.get()
            if elemento == "+":
                numeros.put(primero + ultimo)
            elif elemento == "-":
                numeros.put(primero - ultimo)
            elif elemento == "*":
                numeros.put(primero*ultimo)
            else:
                numeros.put(primero/ultimo)
        else:
            numeros.put(int(elemento))
    return numeros.get()

expresion = "10 40 + 5 * -200 -"
print(evaluarExpresion2(expresion))

#7
def intercalar(pila1:Pila,pila2:Pila) -> Pila:
    res = Pila()
    elementosPila1 = []
    elementosPila2 = []
    while not pila1.empty():
        elementosPila1.append(pila1.get())
    while not pila2.empty():
        elementosPila2.append(pila2.get())
    elementosPila1.reverse()
    elementosPila2.reverse()
    for i in range(0,len(elementosPila1)):
        res.put(elementosPila1[i])
        res.put(elementosPila2[i])
    for elemento in elementosPila1:
        pila1.put(elemento)
    for elemento in elementosPila2:
        pila2.put(elemento)
    return res

#! PARTE 2: Colas

#8
def generarNrosAlAzar(cantidad:int,desde:int,hasta:int) -> Cola:
    cola = Cola()
    for i in range(0,cantidad):
        numero = random.randint(desde,hasta)
        cola.put(numero)
    return cola
#9
def cantidadDeElementos(cola:Cola) -> int:
    elementos = []
    cantidad = 0
    while not cola.empty():
        elementos.append(cola.get())
        cantidad += 1
    for elem in elementos:
        cola.put(elem)
    return cantidad

#cola = generarNrosAlAzar(10,0,10)
#print(cantidadDeElementos(cola))

#10
def buscarElMaximo(cola:Cola) -> int:
    elementos = []
    maximo = 0
    while not cola.empty():
        valor = cola.get()
        if valor >= maximo:
            maximo = valor
        elementos.append(valor)
    for elem in elementos:
        cola.put(elem)
    return maximo

#cola = generarNrosAlAzar(10,0,100)
#print(buscarElMaximo(cola))

#11
def buscarNotaMinima(cola:Cola)->list[(str,int)]:
    elementos = []
    minimo = cola.get()
    elementos.append(minimo)
    while not cola.empty():
        valor = cola.get()
        if valor[1] <= minimo[1]:
            minimo = valor
        elementos.append(valor)
    for elem in elementos:
        cola.put(elem)
    return minimo

"""
cola = Cola()
cola.put(("Joaquin",10))
cola.put(("Pedro",6))
cola.put(("Juan",7))
cola.put(("Gonza",3))
print(buscarNotaMinima(cola))"""

#12
def intercalar(cola1:Cola,cola2:Cola) -> Cola:
    res = Cola()
    elementos1 = []
    elementos2 = []
    while not cola1.empty():
        elementos1.append(cola1.get())
    while not cola2.empty():
        elementos2.append(cola2.get())
    for elem in elementos1:
            cola1.put(elem)
    for elem in elementos2:
            cola2.put(elem)
    for i in range(0,len(elementos1)):
        res.put(elementos1[i])
        res.put(elementos2[i])
    return res

#13.1
def armarSecuenciaDeBingo() -> Cola:
    cola = Cola()
    secuencia = []
    while len(secuencia) < 100:
        numero = random.randint(0,99)
        if numero not in secuencia:
            secuencia.append(numero)
            cola.put(numero)
    return cola

#13.2
def jugarCartonDeBingo(carton:list[int], bolillero:Cola) -> int:
    cartonCopia = carton.copy()
    jugadas = 0
    elementos = []
    while not bolillero.empty():
        elementos.append(bolillero.get())
    for elem in elementos:
        if len(cartonCopia) == 0:
            break
        if elem not in cartonCopia:
            jugadas += 1
        else:
            jugadas += 1
            cartonCopia.remove(elem)
    for elem in elementos:
        bolillero.put(elem)
    return jugadas

#print(jugarCartonDeBingo([1,99,2,98,67,76,84,35,54,14,11,12],armarSecuenciaDeBingo()))

#14
def pacientesUrgentes(pacientes:Cola) -> int:
    elementos = []
    cantidad = 0
    while not pacientes.empty():
        elementos.append(pacientes.get())
    for elem in elementos:
        if elem[0] < 4:
            cantidad += 1
        pacientes.put(elem)
    return cantidad
""""
pacientes = Cola()
pacientes.put((1,"Juan","Cardiologia"))
pacientes.put((3,"Juan","Cardiologia"))
pacientes.put((2,"Juan","Cardiologia"))
pacientes.put((5,"Juan","Cardiologia"))
pacientes.put((6,"Juan","Cardiologia"))
print(pacientesUrgentes(pacientes))"""

#15
def atencionAClientes(clientes:Cola[tuple[str,int,bool,bool]]) -> Cola[tuple[str,int,bool,bool]]:
    cola = Cola()
    elementos = []
    clientesPrioridad = []
    clientesPreferencial = []
    clientesNormales = []
    while not clientes.empty():
        cliente = clientes.get()
        elementos.append(cliente)
        if (cliente[3]):
            clientesPrioridad.append(cliente)
        elif(cliente[2]):
            clientesPreferencial.append(cliente)
        else:
            clientesNormales.append(cliente)
    for cliente in clientesPrioridad + clientesPreferencial + clientesNormales:
        cola.put(cliente)
    for elem in elementos:
        clientes.put(elem)
    return cola