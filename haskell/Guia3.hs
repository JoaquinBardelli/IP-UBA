--Ejercicio 1)a)
f :: Integer -> Integer
f n | n == 8 = 16 
    | n == 4 = 131
    | n == 16 = 16

--Ejercicio 1)b)
g :: Integer -> Integer
g n | n == 8 = 16 
    | n == 16 = 4
    | n == 131 = 1

--Ejercicio 1)c)
h ::  Integer -> Integer
h n = f(g(n))

k :: Integer -> Integer
k n = g(f(n))

--Ejercicio 2)a)
absoluto :: Integer -> Integer
absoluto n = abs(n)

--Ejercicio 2)b)
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto n m | abs(n) > abs(m) = abs(n)
                   | abs(m) > abs(n) = abs(m)
                   | otherwise = abs (n)

--Ejercicio 2)c)
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | x>=y && x>=z = x
              | y>=x && y>=z = y
              | z>=x && z>=y = z

--Ejercicio 2)d)
algunoEsCero :: Float -> Float -> Bool
algunoEsCero x y = x==0 || y==0

--Ejercicio 2)e)
ambosSonCero :: Float -> Float -> Bool
ambosSonCero x y = x==0 && y==0

--Ejercicio 2)f)
enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo x y = (x<=3 && y<=3) || ((x<=7 && x>3) && (y<=7 && y>3)) || (x>7 && y>7)


--Ejercicio 2)g)
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x/=y && x/=z && y/=z = x + y + z
                    | x/=y && x/=z && y==z = x + y
                    | x==y && x/=z = x + z
                    | x==y && x==z = x

--Ejercicio 2)h)
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y = mod x y == 0

--Ejercicio 2)i)
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod (abs x) 10

--Ejercicio 2)j)
digitoDecenas :: Integer -> Integer
digitoDecenas x = div (mod (abs x) 100 -digitoUnidades x) 10


--Ejercicio 3)
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados x y = mod x y == 0

--Ejericicio 4)a)
productoInterno :: (Integer, Integer) -> (Integer, Integer) -> Integer
productoInterno (a,b) (x,y) = a*x + b*y

--Ejericicio 4)b)
esParMenor :: (Integer, Integer) -> (Integer, Integer) -> Bool
esParMenor (a,b) (x,y) = a<x && b<y

--Ejericicio 4)c)
distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (a,b) (x,y) = sqrt((a-x)^2 + (b-y)^2)
                    
--Ejericicio 4)d)
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (x,y,z) = x+y+z

--Ejericicio 4)e)
{-sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer
sumarSoloMultiplos (x,y,z) n | mod x n ==0 && mod y n ==0 && mod z n ==0 = x+y+z
                             | mod x n ==0 && mod y n ==0 && mod z n /=0 = x+y
                             | mod x n ==0 && mod y n /=0 && mod z n ==0 = x+z
                             | mod x n /=0 && mod y n ==0 && mod z n ==0 = y+z
                             | mod x n ==0 && mod y n /=0 && mod z n /=0 = x
                             | mod x n /=0 && mod y n ==0 && mod z n /=0 = y
                             | mod x n /=0 && mod y n /=0 && mod z n ==0 = z
                             | otherwise = 0-}
                        
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (x,y,z) n = sonMultiplos x n + sonMultiplos y n + sonMultiplos z n
    where 
        sonMultiplos x k
            | k /= 0 && mod x k == 0 = x
            | otherwise = 0

--Ejercicio 4)f)
posPrimerPar :: (Integer, Integer, Integer) -> Integer 
posPrimerPar (x,y,z)
    | mod x 2 == 0 = 1
    | mod y 2 == 0 = 2
    | mod z 2 == 0 = 3
    | otherwise = 4

--Ejercicio 4)g)
crearPar :: a -> b -> (a,b)
crearPar a b = (a,b)

--Ejercicio 4)h)
invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a)


--Ejercicio 5)
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (x,y,z) = (j(x)>l(x)) &&(j(y)>l(y)) && (j(z)>l(z))

j :: Integer -> Integer
j n | n>7 = (2*n)-1
    | otherwise = n^2

l :: Integer -> Integer
l n | n /= 0 && mod n 2 ==0 = div n 2
    | otherwise = (3*n)+1


--Ejercicio 6)
bisiesto:: Integer -> Bool
bisiesto n | mod n 4 /=0 || (mod n 100 ==0 && mod n 400 /= 0) =False
           | otherwise = True

--Ejercicio 7)
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x1,y1,z1) (x2,y2,z2) = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

--Ejercicio 8)
sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos a = digitoDecenas a + digitoUnidades a


comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
             | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0