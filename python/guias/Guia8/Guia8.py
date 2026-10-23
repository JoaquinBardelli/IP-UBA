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

# pila2 = Pila()
# pila2.put(("pedro",6))
# pila2.put(("pedro2",5))
# pila2.put(("pedro3",4))
# pila2.put(("pedro4",8))
# print(buscarNotaMaxima(pila2))
# mostrarPila(pila2)

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

# cola = Cola()
# cola.put(("Joaquin",10))
# cola.put(("Pedro",6))
# cola.put(("Juan",7))
# cola.put(("Gonza",3))
# print(buscarNotaMinima(cola))

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

#! PARTE 3: Diccionarios

#16
def calcularPromedioPorEstudiante(notas: list[tuple[str,float]]) ->dict[str,float]:
    notasEstudiante = {}
    notasPromedio = {}
    for nota in notas:
        if nota[0] not in notasEstudiante:
            notasEstudiante[nota[0]] = []
        notasEstudiante[nota[0]].append(nota[1])
    for estudiante in notasEstudiante: #* Se podia hacer mucho mas facil asi: for estudiante, lista in notasEstudiante.items():
        notasPromedio[estudiante] = sum(notasEstudiante[estudiante])/len(notasEstudiante[estudiante])
    return notasPromedio

#17.1
historiales = {} #Diccionario con clave str y valor Pila[str]

#17.2
def visitarSitio(historiales:dict[str,Pila[str]],usuario:str,sitio:str):
    if usuario in historiales:
        historiales[usuario].put(sitio)
    else:
        historiales[usuario] = Pila()
        historiales[usuario].put(sitio)

#17.3
def navegarAtras(historiales:dict[str,Pila[str]],usuario:str) -> str:
    return historiales[usuario].get()

visitarSitio(historiales,"Joaquin","Google")
visitarSitio(historiales,"Joaquin","Youtube")
visitarSitio(historiales,"Joaquin","Spotify")
visitarSitio(historiales,"Pedro","Google")
print(historiales)
navegarAtras(historiales,"Joaquin")

#18
inventario = {}  #Es un diccionario con clave nombre del producto y valor otro diccionario con clave precio o cantidad (y valor el contrario, si precio es clave, cantidad valor y viceversa), siendo de tipo float e int respectivamente

#18.1
def agregarProducto(inventario:dict[str,dict[str, int | float]],nombre:str,precio:float,cantidad:int):
    inventario[nombre] = {}
    inventario[nombre]["precio"] = precio
    inventario[nombre]["cantidad"] = cantidad

#18.2
def actualizarStock(inventario:dict[str,dict[str, int | float]],nombre:str,cantidad:int):
    inventario[nombre]["cantidad"] = cantidad

#18.3
def actualizarPrecio(inventario:dict[str,dict[str, int | float]],nombre:str,precio:float):
    inventario[nombre]["precio"] = precio

#18.4
def calcularValorInventario(inventario:dict[str,dict[str, int | float]]) -> float:
    valor = 0.0
    for producto in inventario:                       #* Tambien se podria haber hecho como: for datos in inventario.values():
        cantidad = inventario[producto]["cantidad"]                                        #*   valor += datos["cantidad"] * datos["precio"]
        precio = inventario[producto]["precio"]
        valor += cantidad*precio
    return valor

inventario = {}
agregarProducto(inventario, "Camisa", 20.0, 50)
agregarProducto(inventario, "Pantalón", 30.0, 30)
actualizarStock(inventario, "Camisa", 10)
valorTotal = calcularValorInventario(inventario)
print("Valor total del inventario:", valorTotal)   # 1100.0


#! PARTE 4: Archivos

puntuacion = ".,;:“”‘’\"'¡!¿?()[]{}<>"

#19.1
def contarLineas(nombreArchivo: str) -> int:
    archivo = open(nombreArchivo, "r", encoding="utf-8")
    cantidad = 0
    for linea in archivo:
        cantidad += 1
    archivo.close()
    return cantidad

#print(contarLineas("prueba.txt"))   # 19

#19.2
def existePalabra(nombreArchivo:str,palabra:str) -> bool:
    archivo = open(nombreArchivo, "r", encoding="utf-8")
    existe = False
    for linea in archivo:
        for signo in puntuacion:
            linea = linea.replace(signo, " ")
        if palabra in linea.split():
            existe = True
            break
    archivo.close()
    return existe

# print(existePalabra("prueba.txt", "Hola"),      # True  (aparece como "Hola!")
# existePalabra("prueba.txt", "ip-algo1"),  # True  (el guion es parte de la palabra)
# existePalabra("prueba.txt", "canción"),   # True  (con tilde)
# existePalabra("prueba.txt", "cas") ,      # False (solo está dentro de "casa")
# existePalabra("prueba.txt", "gato") )     # False

#19.3
def cantidadDeApariciones(nombreArchivo:str,palabra:str) -> int:
    archivo = open(nombreArchivo, "r", encoding="utf-8")
    cantidad = 0
    for linea in archivo:
        for signo in puntuacion:
            linea = linea.replace(signo, " ")
        cantidad += linea.split().count(palabra)
    archivo.close()
    return cantidad

# print(contarLineas("prueba.txt"))                      # 19
# print(existePalabra("prueba.txt", "Hola"))             # True
# print(existePalabra("prueba.txt", "cas"))              # False
# print(cantidadDeApariciones("prueba.txt", "casa"))     # 3

#20
def agruparPorLongitud(nombreArchivo:str) -> dict[int,int]:
    cantidades = {}
    longPalabras = longitudDePalabras(nombreArchivo)
    for i in longPalabras:
        if i in cantidades:
            cantidades[i] += 1
        else:
            cantidades[i] = 1
    return cantidades

def longitudDePalabras(nombreArchivo:str) -> list[int]:
    long = []
    archivo = open(nombreArchivo,"r", encoding='utf-8')
    for linea in archivo:
        for signo in puntuacion:
            linea = linea.replace(signo, " ")
        for palabra in linea.split():
            long.append(len(palabra))
    archivo.close()
    return long

#print(agruparPorLongitud("prueba.txt"))

#21
def laPalabraMasFrecuente(nombreArchivo:str) -> str:
    frecuencia = frecuenciaPalabra(nombreArchivo)
    maximo = 0
    masFrecuente = ""
    for palabra in frecuencia:
        if frecuencia[palabra] > maximo:
            maximo = frecuencia[palabra]
            masFrecuente = palabra
    return masFrecuente

def frecuenciaPalabra(nombreArchivo:str) -> dict[str,int]:
    frecuencia = {}   
    archivo = open(nombreArchivo,"r",encoding="utf-8")
    for linea in archivo:
        for signo in puntuacion:
            linea = linea.replace(signo," ")
        for palabra in linea.split():
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
    archivo.close()
    return frecuencia

#print(laPalabraMasFrecuente("prueba.txt"))

#22
def clonarSinComentarios(nombreArchivoEntrada:str,nombreArchivoSalida:str):
    entrada = open(nombreArchivoEntrada,"r",encoding="utf-8")
    salida = open(nombreArchivoSalida,"w",encoding="utf-8")
    for linea in entrada:
        if linea[0] != "#":
            salida.write(linea)
    entrada.close()
    salida.close()

#clonarSinComentarios("prueba.txt","pruebaSinComentarios.txt")

#23
def invertirLineas(nombreArchivoEntrada:str,nombreArchivoSalida:str):
    entrada = open(nombreArchivoEntrada,"r",encoding="utf-8")
    salida = open(nombreArchivoSalida,"w",encoding="utf-8")
    lineas = entrada.readlines()
    for i in range(len(lineas)-1,-1,-1):
        salida.write(lineas[i])
    entrada.close()
    salida.close()

# invertirLineas("prueba.txt","pruebaLineasInvertidas.txt")

#24
def agregarFraseAlFinal(nombreArchivo:str,frase:str):
    archivo = open(nombreArchivo,"r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    archivo2 = open(nombreArchivo,"a",encoding="utf-8")
    if len(lineas) > 0 and not lineas[len(lineas)-1].endswith("\n"):
        archivo2.write("\n")
    archivo2.write(frase + "\n")
    archivo2.close()

#agregarFraseAlFinal("prueba.txt","Agrego esta frase al final")

#25
def agregarFraseAlPrincipio(nombreArchivo:str,frase:str):
    nuevo = [frase + "\n"]
    archivo = open(nombreArchivo,"r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    nuevo = nuevo + lineas
    archivo2 = open(nombreArchivo,"w", encoding="utf-8")
    for linea in nuevo:
        archivo2.write(linea)
    archivo2.close()

#agregarFraseAlPrincipio("prueba.txt", "Esta es la nueva primera linea")

#26
def listarTextosDeArchivo(nombreArchivo:str) -> list[str]:
    archivo = open(nombreArchivo, "rb")
    resultado = []
    actual = ""
    contenido = archivo.read()
    archivo.close()
    for byte in contenido:
        c = chr(byte)
        if c.isalnum() or c == " " or c == "_":
            actual += c
        else:
            if len(actual) >= 5:
                resultado.append(actual)
            actual = ""
    if len(actual) >= 5:
        resultado.append(actual)
    return resultado

#27
def calcularPromedioPorEstudiante(nombreArchivoNotas : str, nombreArchivoPromedios : str):
    archivo = open(nombreArchivoNotas, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    promedioPorEstudiante = {}
    for linea in lineas:
        if linea.strip() == "":
            continue
        campos = linea.split(",")
        if campos[0] not in promedioPorEstudiante:
            promedioPorEstudiante[campos[0]] = promedioEstudiante(lineas, campos[0])
    promedios = open(nombreArchivoPromedios, "w", encoding="utf-8")
    for lu, promedio in promedioPorEstudiante.items():
        promedios.write(lu + "," + str(promedio) + "\n")
    promedios.close()
    

def promedioEstudiante(notasDeEstudiantes : list[str], lu : str) -> float:
    sumaNotas = 0
    cantidad = 0
    for elemento in notasDeEstudiantes:
        if elemento.strip() == "":
            continue
        campos = elemento.split(",")
        if campos[0] == lu:
            sumaNotas += float(campos[3])
            cantidad += 1
    return sumaNotas/cantidad

calcularPromedioPorEstudiante("notas.txt", "promedioNotas.txt")