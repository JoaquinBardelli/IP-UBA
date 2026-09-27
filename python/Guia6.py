import math 

#EJERCICIOS A
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

#EJERCICIOS B
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

#EJERCICIOS C
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

#EJERCICIOS D
