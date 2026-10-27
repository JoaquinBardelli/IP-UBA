import random
from queue import Queue as Cola

#! PARTE 2: Colas

#8
def generarNrosAlAzarCola(cantidad:int,desde:int,hasta:int) -> Cola:
    cola = Cola()
    for i in range(0,cantidad):
        numero = random.randint(desde,hasta)
        cola.put(numero)
    return cola
#9
def cantidadDeElementosCola(cola:Cola) -> int:
    elementos = []
    cantidad = 0
    while not cola.empty():
        elementos.append(cola.get())
        cantidad += 1
    for elem in elementos:
        cola.put(elem)
    return cantidad

#cola = generarNrosAlAzarCola(10,0,10)
#print(cantidadDeElementosCola(cola))

#10
def buscarElMaximoCola(cola:Cola) -> int:
    elementos = []
    maximo = cola.get()
    elementos.append(maximo)
    while not cola.empty():
        valor = cola.get()
        if valor >= maximo:
            maximo = valor
        elementos.append(valor)
    for elem in elementos:
        cola.put(elem)
    return maximo

#cola = generarNrosAlAzarCola(10,0,100)
#print(buscarElMaximoCola(cola))

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

# cola = Cola()
# cola.put(("Joaquin",10))
# cola.put(("Pedro",6))
# cola.put(("Juan",7))
# cola.put(("Gonza",3))
# print(buscarNotaMinima(cola))

#12
def intercalarCola(cola1:Cola,cola2:Cola) -> Cola:
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

# pacientes = Cola()
# pacientes.put((1,"Juan","Cardiologia"))
# pacientes.put((3,"Juan","Cardiologia"))
# pacientes.put((2,"Juan","Cardiologia"))
# pacientes.put((5,"Juan","Cardiologia"))
# pacientes.put((6,"Juan","Cardiologia"))
# print(pacientesUrgentes(pacientes))

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

