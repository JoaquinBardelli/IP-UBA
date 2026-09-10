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

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (x:xs) = (x+n):sumarN n xs

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