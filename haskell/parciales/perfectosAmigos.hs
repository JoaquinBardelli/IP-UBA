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