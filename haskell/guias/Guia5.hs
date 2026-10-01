module Guia5 where

fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib(n-1) + fib(n-2)


-- Ejercicio 1
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

ultimo :: [t] -> t
ultimo x | longitud x == 1 = head x
         | longitud x > 1 = ultimo (tail x)
         | otherwise = error "La lista esta vacia"

principio :: [t] -> [t]
principio x | longitud x == 1 = []
            | otherwise = head x : principio (tail x)

reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]

--
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece t x | longitud x == 0 = False
              | t == head x = True
              | otherwise = pertenece t (tail x)

todosIguales :: (Eq t) => [t]-> Bool
todosIguales [] = False 
todosIguales [x] = True
todosIguales (x:xs) | x == head xs = todosIguales xs
                    | otherwise = False

todosDistintos :: (Eq t) => [t]-> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:xs) | x /= head xs = todosDistintos xs
                      | otherwise = False

hayRepetidos :: (Eq t) => [t]-> Bool
hayRepetidos [x] = False
hayRepetidos (x:xs) | hayRepetidosAux x xs == True = True
                    | otherwise = hayRepetidos xs

hayRepetidosAux :: (Eq t) => t -> [t]-> Bool
hayRepetidosAux n [] = False
hayRepetidosAux  n lista  | n /= head lista = hayRepetidosAux n (tail lista)
                          | otherwise = True

quitar :: (Eq t) => t-> [t]-> [t]
quitar n [] = []
quitar n (x:xs) | n == x = xs
                | otherwise = x : quitar n xs

quitarTodos :: (Eq t ) => t-> [t]-> [t]
quitarTodos n [] = []
quitarTodos n (x:xs) | n == x = quitarTodos n xs
                     | otherwise = x : quitarTodos n xs 

eliminarRepetidos :: (Eq t) => [t]-> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | hayRepetidos (x:xs) == False = (x:xs)
                         | otherwise = x : eliminarRepetidos (quitarTodos x xs)

mismosElementos :: (Eq t) => [t]-> [t]-> Bool
mismosElementos [] [] = True
mismosElementos (x:xs) lista2 | pertenece x lista2 = mismosElementos (quitarTodos x xs) (quitarTodos x lista2)
                              | otherwise = False

capicua :: (Eq t) => [t]-> Bool
capicua lista | lista == reverso lista = True
              | otherwise = False 

-- Ejercicio 2
sumatoria :: [Integer]-> Integer
sumatoria [] = 0
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs

productoria :: [Integer] -> Integer
productoria [] = 0
productoria [x] = x
productoria (x:xs) = x * productoria xs

maximo :: [Integer]-> Integer
maximo [x] = x
maximo (x:xs) | x >= head xs = maximoAux x (tail xs)
              | otherwise = maximo xs

maximoAux :: Integer -> [Integer] -> Integer
maximoAux n [] = n
maximoAux n (x:xs) | n >= x = maximoAux n xs
                   | otherwise = maximoAux x xs

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (x:xs) = (x+n):sumarN n xs

sumarElPrimero :: [Integer]-> [Integer]
sumarElPrimero lista = sumarN (head lista) lista

sumarElUltimo :: [Integer]-> [Integer]
sumarElUltimo lista = sumarN (ultimo lista) lista

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs

multiplosDeN :: Integer-> [Integer]-> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

ordenar :: [Integer]-> [Integer]
ordenar [x] = [x]
ordenar lista = ordenar (quitar max lista) ++ [max]
    where
        max = maximo lista 

-- Ejercicio 3
sacarBlancosRepetidos :: [Char]-> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:xs) | x == ' ' && x == (head xs) = x : sacarBlancosRepetidos (tail xs)
                             | x == ' ' && x /= (head xs) = x : sacarBlancosRepetidos xs
                             | otherwise = x : sacarBlancosRepetidos xs

contarPalabras :: [Char]-> Integer
contarPalabras [] = 0
contarPalabras [x] | x == ' ' = 0
                   | otherwise = 1
contarPalabras (x:xs) | x == ' ' = contarPalabras xs
                      | (head xs) == ' ' = 1 + contarPalabras (tail xs)
                      | otherwise = contarPalabras xs

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras (x:xs) 
    | x == ' '      = palabras xs
    | otherwise     = tomarPalabra (x:xs) : palabras (sacarPalabara (x:xs))

tomarPalabra :: [Char] -> [Char]
tomarPalabra [] = []
tomarPalabra (y:ys) 
    | y == ' '      = []
    | otherwise     = y : tomarPalabra ys

sacarPalabara :: [Char] -> [Char]
sacarPalabara [] = []
sacarPalabara (y:ys) 
    | y == ' '      = ys
    | otherwise     = sacarPalabara ys

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga lista 
    | tomarPalabra (sacarPalabara lista) == [] = tomarPalabra lista
    | longitud primera >= longitud segunda       = palabraMasLarga (primera ++ [' '] ++ sacaDos)
    | otherwise                                = palabraMasLarga (sacarPalabara lista)
    where 
        primera = tomarPalabra lista
        segunda = tomarPalabra (sacarPalabara lista)
        sacaDos = sacarPalabara (sacarPalabara lista)

-- Ejercicio 4
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [x] = [x]
sumaAcumulada (x:y:xs) = x : sumaAcumulada ((x + y):xs)

                    
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = descomponer x : descomponerEnPrimos xs


descomponer :: Integer -> [Integer]
descomponer n | n == 1 = []
              | otherwise = (menorDivisorPrimo n 2) : descomponer (div n (menorDivisorPrimo n 2))



esPrimo :: Integer -> Bool
esPrimo n | n < 2 = False
          | menorDivisor n == n = True
          | otherwise = False

menorDivisor :: Integer -> Integer
menorDivisor n | n == 1 = 1
               | otherwise = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n k | mod n k == 0 = k
                      | otherwise = menorDivisorDesde n (k+1)

menorDivisorPrimo :: Integer -> Integer -> Integer
menorDivisorPrimo n k | mod n k == 0 && esPrimo k = k
                      | otherwise = menorDivisorPrimo n (k+1)


-- Ejercicio 6
--a) Implementar una funcion que me diga si una persona aparece en mi lista de contactos del telefono
--b) Implementar una funcion que agregue una nueva persona a mis contactos, si esa persona esta ya en mis contactos entonces actualiza el telefono.
--c) Implementar una funcion que dado un nombre, elimine un contacto de mis contactos. Si esa persona no esta no hace nada.

type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

elNombre :: Contacto -> Nombre 
elNombre (nombre, telefono) = nombre 

elTelefono :: Contacto -> Nombre
elTelefono (nombre, telefono) = telefono 

enLosContactos :: Nombre-> ContactosTel-> Bool
enLosContactos nombre [] = False
enLosContactos nombre ((nombreContacto, telefono):xs) | nombre == nombreContacto = True
                                                      | otherwise = enLosContactos nombre xs

agregarContacto :: Contacto-> ContactosTel-> ContactosTel
agregarContacto contacto [] = []
agregarContacto contacto (existente:xs) | elNombre contacto == elNombre existente = (elNombre existente, elTelefono contacto) : xs
                                        | otherwise = (elNombre existente, elTelefono existente) : agregarContacto contacto xs

eliminarContacto :: Nombre-> ContactosTel-> ContactosTel
eliminarContacto nombre [] = []
eliminarContacto nombre (x:xs) | nombre == elNombre x = xs
                               | otherwise = x : eliminarContacto nombre xs

--Ejercicio 8
--a
sumaTotal :: [[Integer]]-> Integer
sumaTotal [] = 0
sumaTotal (lista:xs) = sumarElementos lista + sumaTotal xs

sumarElementos :: [Integer] -> Integer
sumarElementos [] = 0
sumarElementos (x:xs) = x + sumarElementos xs

--b
cantidadDeApariciones :: Integer-> [[Integer]]-> Integer
cantidadDeApariciones n [] = 0
cantidadDeApariciones n (lista:xs) = cantidadDeAparicionesLista n lista + cantidadDeApariciones n xs 

cantidadDeAparicionesLista :: Integer -> [Integer] -> Integer
cantidadDeAparicionesLista n [] = 0
cantidadDeAparicionesLista n (x:xs) | n == x = 1 + cantidadDeAparicionesLista n xs
                                    | otherwise = cantidadDeAparicionesLista n xs

--c
contarPalabras2 :: String -> [[String]] -> Int
contarPalabras2 palabra [] = 0 
contarPalabras2 palabra (oracion:xs) = contarApariciones palabra oracion + contarPalabras2 palabra xs

contarApariciones :: String -> [String] -> Int
contarApariciones palabra [] = 0
contarApariciones palabra (x:xs) | palabra == x = 1 + contarApariciones palabra xs
                                 | otherwise = contarApariciones palabra xs

--d
cantidadDeApariciones2 :: (Eq a) => a-> [[a]]-> Integer
cantidadDeApariciones2 elemento [] = 0
cantidadDeApariciones2 elemento (x:xs) = contarAparicionesLista2 elemento x + cantidadDeApariciones2 elemento xs

contarAparicionesLista2 :: (Eq a) => a-> [a]-> Integer
contarAparicionesLista2 elemento [] = 0 
contarAparicionesLista2 elemento (x:xs) | elemento == x = 1 + contarAparicionesLista2 elemento xs
                                        | otherwise = contarAparicionesLista2 elemento xs

-- e
multiplicarPorEscalar :: Integer-> [[Integer]]-> [[Integer]]
multiplicarPorEscalar escalar [] = []
multiplicarPorEscalar escalar (x:xs) = multiplicarPorEscalarLista escalar x : multiplicarPorEscalar escalar xs

multiplicarPorEscalarLista :: Integer -> [Integer] -> [Integer]
multiplicarPorEscalarLista escalar [] = []
multiplicarPorEscalarLista escalar (x:xs) = escalar*x : multiplicarPorEscalarLista escalar xs

--f
concatenarFilas :: [[String]]->[String]
concatenarFilas [] = []
concatenarFilas (x:xs) = concatenarStrings x : concatenarFilas xs

concatenarStrings :: [String] -> String
concatenarStrings [] = ""
concatenarStrings (x:xs) = x ++ concatenarStrings xs 

--g
iesimaFila :: Integer-> [[a]]-> [a]
iesimaFila n (x:xs) | n == 1 = x
                    | otherwise = iesimaFila (n-1) xs

--h
iesimaColumna :: Integer -> [[a]] -> [a]
iesimaColumna n [] = []
iesimaColumna n (x:xs) = columnaAux n x : iesimaColumna n xs

columnaAux :: Integer -> [a] -> a
columnaAux n (x:xs) | n == 1 = x
                    | otherwise = columnaAux (n-1) xs

--i
matrizIdentidad :: Integer-> [[Integer]]
matrizIdentidad 0 = []
matrizIdentidad tamano = armarIdentidad 1 tamano


armarIdentidad :: Integer -> Integer -> [[Integer]]
armarIdentidad posicion 0 = []
armarIdentidad posicion tamano | posicion <= tamano = armarFila posicion tamano : armarIdentidad (posicion + 1) tamano
                               | otherwise = []
armarFila :: Integer -> Integer -> [Integer]
armarFila posicion 0 = []
armarFila posicion tamano | posicion == 1 = 1 : armarFila 0 (tamano-1)
                          | otherwise = 0 : armarFila (posicion-1) (tamano-1)

--j
cantidadParesColumna :: Integer-> [[Integer]]-> Integer
cantidadParesColumna columna matriz = cantidadPares (iesimaColumna columna matriz)

cantidadPares :: [Integer] -> Integer
cantidadPares [] = 0
cantidadPares (x:xs) | mod x 2 == 0 = 1 + cantidadPares xs
                     | otherwise = cantidadPares xs 