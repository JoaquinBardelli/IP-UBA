from queue import LifoQueue as Pila

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