-- EJERCICIO 1 (2 puntos)
-- problema mediaMovilN (lista: seq⟨Z⟩, n: Z) : Float {
--   requiere: {|lista| > 0}
--   requiere: {n > 0 ∧ n ≤ |lista|}
--   asegura: {res es el promedio de los últimos n elementos de lista}
-- }

mediaMovilN :: [Integer] -> Integer -> Float
mediaMovilN lista n = fromIntegral(sumarElementos(agarrarUltimosN lista n))/ (fromIntegral n)

agarrarUltimosN :: [Integer] -> Integer -> [Integer]
agarrarUltimosN lista n | n == (longitud lista) = lista
                        | otherwise = agarrarUltimosN (tail lista) n


longitud :: [Integer] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs


sumarElementos :: [Integer] -> Integer
sumarElementos [] = 0
sumarElementos (x:xs) = x + sumarElementos xs


-- EJERCICIO 2 (2 puntos)    n>0
-- problema esAtractivo (n: Z) : Bool {
--   requiere: {n > 0}
--   asegura: {res = true <=> la cantidad de factores primos de n (distintos o no) es también un número primo.}
-- }
-- Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3]. 

esAtractivo :: Integer -> Bool
esAtractivo n | esPrimo(longitud(factoresPrimos n 2)) = True
              | otherwise = False

esPrimo :: Integer -> Bool
esPrimo n = n > 1 && longitud(divisores n 2) == 1

divisores:: Integer -> Integer -> [Integer]
divisores 0 _ = []
divisores 1 _ = [1]
divisores n d | d > n = []
              | mod n d == 0 = d : divisores n (d+1)
              | otherwise = divisores n (d+1)

factoresPrimos :: Integer -> Integer -> [Integer]
factoresPrimos 0 _ = []
factoresPrimos 1 _ = []
factoresPrimos n d | d > n = []
                   | mod n d == 0 && (esPrimo d) = d : factoresPrimos (div n d) d
                   | otherwise = factoresPrimos n (d+1)


-- EJERCICIO 3 (2 puntos)
-- problema palabraOrdenada (palabra: seq⟨Char⟩) : Bool {
--   requiere: {True}
--   asegura: {res = true <=> cada uno de los elementos no blancos de palabra es mayor o igual al anterior caracter no blanco, si existe alguno.}
-- }
-- Aclaración: 'a' < 'b' es True. 

palabraOrdenada :: [Char] -> Bool
palabraOrdenada [x] = True
palabraOrdenada (x:y:xs) | x /= ' ' && y /= ' ' && x <= y = palabraOrdenada (y:xs) 
                         | x == ' ' && y /= ' ' = palabraOrdenada (y:xs)
                         | x /= ' ' && y == ' ' = palabraOrdenada (x:xs)
                         | x == ' ' && y == ' ' = palabraOrdenada xs
                         | otherwise = False




-- EJERCICIO 4 (3 puntos)
-- problema similAnagrama (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Bool⟩{
--   requiere: {True}
--   asegura: {res = true <=> (para todo caracter no blanco, la cantidad de apariciones de ese caracter en palabra1 es igual a la cantidad de apariciones en palabra2, y además existe al menos un caracter en palabra1 que tiene una posición distinta en palabra2)}
-- } 

similAnagrama :: [Char] -> [Char] -> Bool
similAnagrama palabra1 palabra2 | (todosMismaCantidad palabra1 palabra2) && (hayDistinta palabra1 palabra2) = True
                                | otherwise = False



hayDistinta :: [Char] -> [Char] -> Bool
hayDistinta palabra1 palabra2 = hayPosicionDistinta (sacarBlancos palabra1) (sacarBlancos palabra2)

hayPosicionDistinta :: [Char] -> [Char] -> Bool
hayPosicionDistinta [] _ = False
hayPosicionDistinta (x:xs) (y:ys) | x /= y = True
                                  | otherwise = hayPosicionDistinta xs ys

todosMismaCantidad :: [Char] -> [Char] -> Bool
todosMismaCantidad [] palabra = True  --ESTA LINEA ESTA MAL, TENDRIA QUE SER: todosMismaCantidad [] palabra = largo (sacarBlancos palabra) == 0
todosMismaCantidad (x:xs) palabra2 | mismaCantidadApariciones x (x:xs) palabra2 = todosMismaCantidad sacado1 sacado2
                                   | otherwise = False
                                   where
                                    sacado1 = sacarCaracter x (x:xs)
                                    sacado2 = sacarCaracter x palabra2


sacarCaracter :: Char -> [Char] -> [Char]
sacarCaracter c [] = []
sacarCaracter c (x:xs) | c == x = sacarCaracter c xs
                       | otherwise = x : sacarCaracter c xs

mismaCantidadApariciones :: Char -> [Char] -> [Char] -> Bool
mismaCantidadApariciones c [] [] = True
mismaCantidadApariciones c primera segunda | (largo palabra1) /= (largo palabra2) = False
                                           | (cantidadApariciones c palabra1) == (cantidadApariciones c palabra2) = True
                                           | otherwise = False
                                           where
                                            palabra1 = sacarBlancos primera
                                            palabra2 = sacarBlancos segunda


cantidadApariciones :: Char -> [Char] -> Integer
cantidadApariciones _ [] = 0
cantidadApariciones c (x:xs) | c == x = 1 + cantidadApariciones c xs
                             | otherwise = cantidadApariciones c xs

sacarBlancos :: [Char] -> [Char]
sacarBlancos [] = []
sacarBlancos (x:xs) | x == ' ' = sacarBlancos xs
                    | otherwise = x : sacarBlancos xs 

largo :: [Char] -> Integer
largo [] = 0
largo (x:xs) = 1 + largo xs