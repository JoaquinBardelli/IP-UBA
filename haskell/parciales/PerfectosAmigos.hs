--Ejercicio 1

{-problema divisoresPropios (n: Z) : seq⟨Z⟩ {
    requiere: {n > 0}
    asegura: {res contiene a todos los divisores propios de n, ordenados de menor a mayor}
    asegura: {res no tiene elementos repetidos}
    asegura: {res no contiene a ning´un elemento que no sea un divisor propio de n}
}
-}

divisoresPropios :: Int->[Int]
divisoresPropios n = divisores n 1

divisores :: Int -> Int -> [Int]
divisores 1 _ = [1]
divisores n d | n == d = []
              | mod n d == 0 = d : divisores n (d+1)
              | otherwise = divisores n (d+1)

{-problema sonAmigos (n,m: Z) : Bool {
    requiere: {n > 0}
    requiere: {m > 0}
    requiere: {m̸ = n}
    asegura: {res = True ⇔ n y m son n´umeros amigos}
}

Dos n´umeros naturales distintos son amigos si cada uno de ellos se obtiene sumando los divisores propios del otro.
Por ejemplo, 220 y 284 son amigos porque los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110 que
sumados dan 284 y los divisores propios de 284 son 1, 2 , 4, 71, 142 que sumados dan 220.
-}
sonAmigos :: Int -> Int -> Bool
sonAmigos a b = sumaDivisores(divisoresPropios a) == b && sumaDivisores(divisoresPropios b) == a


sumaDivisores :: [Int] -> Int
sumaDivisores [] = 0 
sumaDivisores (x:xs) = x + sumaDivisores xs

{-problema losPrimerosNPerfectos (n: Z) : seq⟨Z⟩ {
    requiere: {n > 0}
    asegura: {|res| = n}
    asegura: {res es la lista de los primeros n n´umeros perfectos, de menor a mayor}
}
-}

losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos num = primerosNPerfectos num 1


primerosNPerfectos :: Int -> Int -> [Int]
primerosNPerfectos cant num | cant == 0 = []
                            | esPerfecto num = num : primerosNPerfectos (cant-1) (num + 1)
                            | otherwise = primerosNPerfectos cant (num + 1)

esPerfecto :: Int -> Bool
esPerfecto 1 = False
esPerfecto num = sumaDivisores(divisoresPropios num) == num

{-problema listaDeAmigos (lista: seq⟨Z⟩) : seq⟨Z × Z⟩ {
    requiere: {Todos los n´umeros de lista son mayores a 0}
    requiere: {Todos los n´umeros de lista son distintos}
    asegura: {res es una lista de tuplas sin repetidos, que contiene a todos los pares de n´umeros que pertenecen a lista
    y son amigos entre s´ı}
    asegura: {|res| es igual a la cantidad de pares de n´umeros amigos que hay en lista.}
}-}

listaDeAmigos :: [Int] -> [(Int,Int)]
listaDeAmigos [] = []
listaDeAmigos (x:xs) = listarAmigos (x:xs) ++ listaDeAmigos xs

listarAmigos :: [Int] -> [(Int,Int)]
listarAmigos [x] = []
listarAmigos (x:xs) | (sonAmigos x (head xs)) = (x, head xs) : listarAmigos (x:(tail xs))
                    | otherwise = listarAmigos (x : (tail xs))