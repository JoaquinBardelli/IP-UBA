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

sacarBlancosRepetidos :: [Char]-> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:xs) | x == ' ' && x == (head xs) = x : sacarBlancosRepetidos (tail xs)
                             | x == ' ' && x /= (head xs) = x : sacarBlancosRepetidos xs
                             | otherwise = x : sacarBlancosRepetidos xs

contarPalabras :: [Char]-> Integer
contarPalabras [] = 0
contarPalabras [x] | [x] == ' ' = 0
                   | otherwise = 1
contarPalabras (x:xs) | x == ' ' = contarPalabras xs
                      | (head xs) == ' ' = 1 + contarPalabras (tail xs)
                      | otherwise = contarPalabras xs
                            
                    