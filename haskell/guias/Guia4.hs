fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n-2)

parteEntera :: Float -> Integer
parteEntera n | n >= 0    = floor n
              | otherwise = 0

esDivisible :: Integer -> Integer -> Bool
esDivisible n m | n == 0 = True
                | n < 0 = False
                | otherwise = esDivisible (n-m) m

medioFact :: Integer -> Integer
medioFact n | n == 0 = 0
            | n == 1 = 1
            | n == 2 = 2
            | otherwise = n*medioFact(n-2)

factorial :: Integer -> Integer
factorial n | n == 0 = 1
            | otherwise = n*factorial(n-1)


digitoUnidades :: Integer -> Integer
digitoUnidades x = mod (abs x) 10

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | ultimo ==  anteultimo = todosDigitosIguales(div(n - ultimo) 10) 
                      | otherwise = False
                      where
                        ultimo = digitoUnidades n
                        anteultimo = digitoUnidades(div(n-digitoUnidades n) 10)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | n >= 0 && i >= 1 && i <=  cantDigitos n = mod (div n (10^((cantDigitos n) -i)))  10
                 | otherwise = 0


cantDigitos :: Integer -> Integer
cantDigitos n | abs n < 10 = 1
              | otherwise = 1 + cantDigitos (div n 10)

sumaDigitos :: Integer -> Integer
sumaDigitos n |  abs n < 10 = n
              | otherwise = iesimoDigito n (cantDigitos n) + sumaDigitos (div n 10)

{-esCapicua :: Integer -> Bool
esCapicua n | numero < 10 = True
            | primero == ultimo = esCapicua recortado
            | otherwise = False
            where
              numero = abs n
              primero = iesimoDigito numero 1
              ultimo = iesimoDigito numero (cantDigitos numero)
              recortado = div (numero - (primero*(10^(cantDigitos numero -1))) - ultimo) 10-}

invertir :: Integer -> Integer -> Integer
invertir 0 acumulado = acumulado
invertir n acumulado = invertir (div n 10) (acumulado * 10 + mod n 10)

esCapicua :: Integer -> Bool
esCapicua n = numero == invertir numero 0
  where
    numero = abs n

sumatoria2i :: Integer -> Integer
sumatoria2i 0 = 1
sumatoria2i n = 2^n + sumatoria2i (n-1)

sumatoriaQi :: Integer -> Integer -> Integer
sumatoriaQi q 1 = q
sumatoriaQi q n = q^n + sumatoriaQi q (n-1)

sumatoria2Qi :: Integer -> Integer -> Integer
sumatoria2Qi q 0 = 0
sumatoria2Qi q n = sumatoriaQi q (2*n)

sumatoriaD :: Integer -> Integer -> Integer
sumatoriaD q 0 = 1
sumatoriaD q n = sumatoria2Qi q n - sumatoriaQi q (n-1)

eAprox :: Integer -> Float
eAprox n | n == 0 = 1
         | otherwise = (1/(fromIntegral(factorial n))) + eAprox(n-1)

e :: Float
e = eAprox 10

-- Sucesión auxiliar a_n
sucesionA :: Integer -> Float
sucesionA 1 = 2
sucesionA n = 2 + (1 / sucesionA (n - 1))

-- Aproximación final (a_n - 1)
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = sucesionA n - 1


{-sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = (sumaSimple q n) * (sumaSimple q m)


sumaSimple :: Integer -> Integer -> Integer
sumaSimple q x | x == 1 = q
| otherwise = q^x + sumaSimple q (x-1)-}

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m | n == 1 = sumaAux q 1 m
| otherwise = sumaAux q n m + sumaPotencias q (n-1) m


sumaAux :: Integer -> Integer -> Integer -> Integer
sumaAux q n m | m == 1 = q^(n+1)
| otherwise = q^(n+m) + sumaAux q n (m-1)

menorDivisor :: Integer -> Integer
menorDivisor n | n == 1 = 1
| otherwise = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n k | mod n k == 0 = k
| otherwise = menorDivisorDesde n (k+1)

esPrimo :: Integer -> Bool
esPrimo n | n == 1 = False
| menorDivisor n == n = True
| otherwise = False

nesimoPrimo :: Integer -> Integer
nesimoPrimo n | n == 1 = 2
| n == 2 = 3
| otherwise = auxiliar n 1

auxiliar :: Integer -> Integer -> Integer
auxiliar n i | n == 0 = i
| esPrimo (i+1) = auxiliar (n-1) (i+1)
| otherwise = auxiliar n (i+1)

esSumaInicialDePrimos:: Integer -> Bool
esSumaInicialDePrimos n | n == 0 = True
| n == 1 = False
| n == 2 = True
| otherwise = sumaInicialPrimosAux n 0

sumaInicialPrimosAux :: Integer -> Integer -> Bool
sumaInicialPrimosAux n m | n < 0 = False
| n == 0 = True
| otherwise = sumaInicialPrimosAux (n - nesimoPrimo(m+1)) (m+1)