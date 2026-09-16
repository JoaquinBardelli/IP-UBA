--Ejercicio 1
f1 :: Integer -> Integer -> Integer
f1 n k | n <= k && esAbundante n = 1 +  f1 (n+1) k
       | n <= k = f1 (n+1) k
       | otherwise = 0


divisoresPropios :: Integer -> Integer ->[Integer]
divisoresPropios 1 k = []
divisoresPropios n  k | n == k = []
                      | n > k && mod n k == 0 = k : divisoresPropios n (k+1)  
                      | otherwise = divisoresPropios n (k+1) 


esAbundante :: Integer -> Bool
esAbundante n | suma > n = True
              | otherwise = False
              where
                suma = sumaElementos(divisoresPropios n 1)

sumaElementos :: [Integer] -> Integer
sumaElementos [] = 0
sumaElementos [x] = x
sumaElementos (x:xs) = x + sumaElementos xs

--Ejercicio 2
f2 :: [(String, Integer, Integer)] -> [String]
f2 [] = []
f2 (x:xs) | estaAprobada x = f2 xs
          | otherwise = (nombreMateria x) : f2 xs
        

estaAprobada :: (String, Integer, Integer) -> Bool
estaAprobada (nombre, ano, cuatri) | ano > 2021 = True
                                   | ano == 2021 && cuatri > 0 = True
                                   | otherwise = False

nombreMateria  :: (String, Integer, Integer) -> String
nombreMateria (nombre, ano, cuatri) = nombre

--Ejercicio 3
f3 :: [Integer] -> Integer -> [Integer]
f3 [] u = []
f3 (x:xs) u | x >= 0 && x <= u = x : f3 xs u
            | x >= 0 && x > u = u : f3 xs u
            | otherwise = []

--Ejercicio 4
f4 :: [[Integer]] -> Integer -> Integer
f4 matriz columna = cantidadPares(recorrerMatriz matriz columna)


recorrerMatriz :: [[Integer]] -> Integer -> [Integer]
recorrerMatriz [] col = []
recorrerMatriz (x:xs) col = (agarrarNElemento x col)  : recorrerMatriz xs col


agarrarNElemento :: [Integer] -> Integer -> Integer
agarrarNElemento (x:xs) elemento | elemento == 1 = x
                                 | otherwise = agarrarNElemento xs (elemento-1)
                                 

cantidadPares:: [Integer] -> Integer
cantidadPares [] = 0
cantidadPares (x:xs) | x == 0 = 1 + cantidadPares xs
                     | mod x 2 == 0 = 1 + cantidadPares xs
                     | otherwise = cantidadPares xs