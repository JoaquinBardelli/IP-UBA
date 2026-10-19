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

print(laPalabraMasFrecuente("prueba.txt"))