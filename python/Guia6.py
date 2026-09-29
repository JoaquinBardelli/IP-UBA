import math 

#EJERCICIOS 1
#Ejercicio 1
def holaMundo():
    print("Hola mundo")

holaMundo()

#Ejercicio 2
def imprimirAmorfoda():
    print("Hoy te odio, no e secreto, ante todo lo confieso \nSi pudiera, te pidiera que devuelva to lo beso que te di \nLa palabra y todo el tiempo que perdi \nMe arrepiento una y mil vece de haber confiao en ti \n")

imprimirAmorfoda()

#Ejercicio 3
def raizDe2():
    print("La raiz de 2 es: ", round(math.sqrt(2),4))

raizDe2()

#Ejercicio 4
def factorialDeDos() -> int:
    return math.factorial(2)

#Ejercicio 5
def perimetro() -> float:
    return math.pi*2

#EJERCICIOS 2
#Ejercicio 1
def imprimirSaludo(nombre: str):
    print("Hola",nombre, "te saluda tu amigo python")

#Ejercicio 2
def raizCuadradaDe(numero:int) -> float:
    if numero > -1:
        return math.sqrt(numero)
    else:
        return math.sqrt(numero*(-1))

#Ejercicio 3
def farenheitACelsius(temp_far:float) -> float:
    return (temp_far-32)*(5/9)

#Ejercicio 4
def imprimirDosVeces(estribillo:str):
    print(estribillo*2)

#Ejercicio 5
def esMultiploDe(numero:int,m:int) -> bool:
    if numero % m == 0:
        return True
    else:
        return False

#Ejercicio 6
def esPar(numero:int) -> bool:
    return esMultiploDe(numero, 2)

#Ejercicio 7
def cantidadDePizzas(comensales:int, minCantDePorciones:int):
    return math.ceil((comensales*minCantDePorciones)/8)

#EJERCICIOS 3
#Ejercicio 1
def algunoEs0(num1:int,num2:int) -> bool:
    if num1 == 0 or num2 == 0:
        return True
    else:
        return False

#Ejercicio 2
def ambosSon0(num1:int,num2:int) -> bool:
    return num1 == 0 and num2 == 0

#Ejercicio 3
def esNombreLargo(nombre:str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

#Ejercicio 4
def esBisiesto(ano:int) -> bool:
    return esMultiploDe(ano, 400) or (esMultiploDe(ano,4) and not esMultiploDe(ano,100))

#EJERCICIOS 4
def pesoPino(altura:int) -> int: #Recibo la altura en metros
    if altura <= 3:
        return altura*100*3
    else:
        return (3*100*3)+((altura-3)*100*2)

def esPesoUtil(peso:int) -> bool:
    return peso >= 400 and peso <= 1000

def sirvePino(altura:int) -> bool:
    return esPesoUtil(pesoPino(altura))


#EJERCICIOS 5
def devolverElDobleSiEsPar(numero:int) -> int:
    if numero % 2 == 0:
        return numero*2
    else:
        return numero

def devolverValorSiEsParSinoElQueSigue(numero:int) -> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero + 1

def devolverElDobleSiEsMultiplo3ElTripleSiEsMultiplo9(numero:int) -> int:
    if numero % 9 == 0:
        return numero*3
    elif numero % 3 == 0:
        return numero*2
    else:
        return numero

def lindoNombre(nombre:str):
    if len(nombre) >= 5:
        print("Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres")

def elRango(numero: int):
    if numero < 5:
        print("Menor a 5")
    elif 10 <= numero <= 20:
        print("Entre 10 y 20")
    elif numero > 20:
        print("Mayor a 20")

def vacacionesOTrabajo(sexo:str, edad:int):
    if sexo == "M" and 18 <= edad <65:
        print("Te toca trabajar")
    elif sexo == "M":
        print("Anda de vacaciones")
    elif sexo == "F" and 18 <= edad <60:
        print("Te toca trabajar")
    else:
        print("Anda de vacaciones")

#EJERCICIOS 6
#Ejercicio 1
def imprimir1a10():
    contador = 1
    while contador <= 10:
        print(contador)
        contador += 1

#Ejercicio 2
def imprimirPares10a40():
    contador = 10
    while contador <= 40:
        if contador % 2 == 0:
            print(contador)
        contador += 1

#Ejercicio 3
def imprimirEcox10():
    contador = 0
    while contador < 10:
        print("eco")
        contador += 1

#Ejercicio 4
def cuentaRegresiva (countdown:int):
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("DESPEGUE")

#Ejercicio 5
def viajarAlPasado(llegada:int,partida:int):
    while partida > llegada + 1:
        print("Viajo un ano al pasado, estamos en el ano", partida-1)
        partida -= 1
    print("Finalmente llego al ano", llegada)

#Ejercicio 6
def conocerAristoteles(llegada:int,partida:int):
    while partida > llegada:
        if partida >= llegada + 20:
            print("Viajo 20 anos al pasado, estamos en el ano",partida-20)
            partida -= 20
        else:
            partida = llegada
    print("Finalmente llego al ano", partida)

conocerAristoteles(-382,-300)

#EJERCICIOS 7
#Ejercicio 1
def imprimir10():
    for i in range(1,11):
        print(i)

#Ejercicio 2
def imprimirPares40():
    for i in range(10,41,2):
        print(i)

#Ejercicio 3
def imprimirEco():
    for i in range(10):
        print("eco")

#Ejercicio 4
def despegue(numero:int):
    for i in range(numero,0,-1):
        print(i)
    print("DESPEGUE")

#Ejercicio 5
def bttf(partida:int,llegada:int):
    for i in range(partida-1,llegada,-1):
        print("Viajo un ano al pasado, estamos en el ano", i)
    print("Finalmente llego al ano", llegada)

#Ejercicio 6
def bttfAris(llegada:int,partida:int):
    for i in range(partida-20,llegada,-20):
        print("Viajo un ano al pasado, estamos en el ano", i)
    print("Finalmente llego al ano", llegada)
