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

agregarFraseAlFinal("prueba.txt","Agrego esta frase al final")

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

agregarFraseAlPrincipio("prueba.txt", "Esta es la nueva primera linea")
