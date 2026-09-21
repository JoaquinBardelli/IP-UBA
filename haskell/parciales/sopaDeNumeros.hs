type Fila = [Int]
type Tablero = [Fila]
type Posicion = (Int, Int)
type Camino = [Posicion]

--1
{-problema maximo (t: Tablero) : Z {
    requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
    menos un elemento}
    requiere: {Existe al menos una columna en el tablero t }
    requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayor estricto a 0}
    asegura: {res es igual al n´umero m´as grande del tablero t}
-}

maximo :: Tablero -> Int
maximo tablero = maximoEnMatriz tablero 1

maximoEnMatriz :: Tablero -> Int -> Int
maximoEnMatriz [] x = x
maximoEnMatriz (x:xs) num | maxFila >= num = maximoEnMatriz xs maxFila
                  | otherwise = maximoEnMatriz xs num
                  where
                    maxFila = maximoEnFila x 1

maximoEnFila :: Fila -> Int -> Int
maximoEnFila [] x = x
maximoEnFila (x:xs) num | x >= num = maximoEnFila xs x
                        | otherwise = maximoEnFila xs num


{-problema masRepetido (t: Tablero) : Z {
    requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
    menos un elemento}
    requiere: {Existe al menos una columna en el tablero t }
    requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayor estricto a 0}
    asegura: {res es igual al n´umero que m´as veces aparece en un tablero t. Si hay empate devuelve cualquiera de ellos}
}-}

{-
1ero agarro un numero de la matriz
2do contar cant de apariciones del numero en la matriz HECHO
3ero guardar el total en una tupla (numero, cantApariciones) HECHO
4to borrar todos esos numeros de la matriz HECHO
5to repetir este proceso hasta que la matriz este vacia e ir comparando tuplas con cantidad de apariciones
-}

masRepetido ::  Tablero -> Int
masRepetido tablero = masRepetidoMatriz tablero (0,0)

masRepetidoMatriz :: Tablero -> (Int, Int) -> Int
masRepetidoMatriz [] (num, apariciones) = num
masRepetidoMatriz (x:xs) (num, apariciones) | x == [] = masRepetidoMatriz xs (num, apariciones)
masRepetidoMatriz tablero (num, apariciones) | apariciones2 >= apariciones = masRepetidoMatriz sacadoMatriz (num2, apariciones2)
                                             | otherwise = masRepetidoMatriz sacadoMatriz (num, apariciones)
                                             where
                                                (num2, apariciones2) = cantAparicionesMatriz tablero primerValor 0
                                                primerValor = darPrimerValor tablero
                                                sacadoMatriz = borrarDeMatriz tablero num2
darPrimerValor :: Tablero -> Int
darPrimerValor (x:xs) | x == [] = darPrimerValor xs
darPrimerValor ((y:ys):xs) = y

borrarDeMatriz :: Tablero -> Int -> Tablero
borrarDeMatriz [] num = []
borrarDeMatriz (x:xs) num = borrarDeFila x num : borrarDeMatriz xs num

borrarDeFila :: Fila -> Int -> Fila
borrarDeFila [] num = []
borrarDeFila (x:xs) num | x == num = borrarDeFila xs num
                        | otherwise = x : borrarDeFila xs num

cantAparicionesMatriz :: Tablero -> Int -> Int -> (Int, Int)
cantAparicionesMatriz [] num apariciones = (num, apariciones)
cantAparicionesMatriz (x:xs) num apariciones = cantAparicionesMatriz xs num (apariciones + aparicionesFila)
                                            where
                                                aparicionesFila = cantAparicionesFila x num

cantAparicionesFila :: Fila -> Int -> Int
cantAparicionesFila [] x = 0
cantAparicionesFila (x:xs) num | x == num = 1 + cantAparicionesFila xs num
                               | otherwise = cantAparicionesFila xs num

{-problema valoresDeCamino (t: Tablero, c: Camino) : seq⟨Z⟩ {
    requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
    menos un elemento}
    requiere: {Existe al menos una columna en el tablero t }
    requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayores estrictos a 0}
    requiere: {El camino c es un camino v´alido, es decir, secuencia de posiciones adyacentes en la que solo es posible
    desplazarse hacia la posici´on de la derecha o hacia abajo y todas las posiciones est´an dentro de los limites del tablero
    t}
    asegura: {res es igual a la secuencia de n´umeros que est´an en el camino c, ordenados de la misma forma que aparecen
    las posiciones correspondientes en el camino.}
    }
-}
{- OBJETIVO: conseguir el valor de cada posicion
1ero Agarrar la fila de la posicion que me dan
2do Agarrar la columna de la posicion que me dan
3ero Devolver el valor de esa fila en esa columna
-}
valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino  tablero [] = []
valoresDeCamino tablero ((numFila, numCol):xs) = columna(fila tablero numFila) numCol : valoresDeCamino tablero xs


fila :: Tablero -> Int -> Fila
fila (x:xs) n | n == 1 = x
              | otherwise = fila xs (n-1)

columna :: Fila -> Int -> Int
columna (x:xs) n | n == 1 = x
                 | otherwise = columna xs (n-1)

{-problema esCaminoFibo (s:seq⟨Z⟩, i : Z) : Bool {
    requiere: {La secuencia de n´umeros s es no vac´ıa y est´a compuesta por n´umeros positivos (mayores estrictos a 0)
    que representan los n´umeros ubicados en las posiciones que forman un camino en un tablero}
    requiere: {i ≥ 0}
    asegura: {res = true ⇔ los valores de s son la sucesi´on de Fibonacci inicializada con el n´umero pasado como
    par´ametro i}
}
-}


{-
1ero armar funcion que haga la secuencia fibo de un n pedido
2do funcion longitud y funcion que me de la secuencia fibo desde un n hasta n + longitud
3ero comparar camino con la funcion pasada
-}

esCaminoFibo :: [Int] -> Int -> Bool
esCaminoFibo camino i | camino == lista = True
                      | otherwise = False
                    where
                        lista = listaFibo i (longitud camino)

fibo :: Int -> Int
fibo 0 = 0
fibo 1 = 1
fibo n = fibo (n-1) + fibo (n-2)

longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

listaFibo :: Int -> Int -> [Int]
listaFibo inicio cantidad | cantidad == 1 = [fibo inicio]
                          | otherwise = fibo inicio : listaFibo (inicio + 1) (cantidad - 1)