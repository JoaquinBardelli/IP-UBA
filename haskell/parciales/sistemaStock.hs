--Ejercicio 1
generarStock :: [String]->[(String, Int)]
generarStock [] = []
generarStock (x:xs) = (x, cantidadVeces x (x:xs)) : generarStock (sacarElemento x (x:xs))
 

cantidadVeces :: String -> [String] -> Int
cantidadVeces cadena [] = 0
cantidadVeces cadena (x:xs) | cadena == x = 1 + cantidadVeces cadena xs
                            | otherwise = cantidadVeces cadena xs

sacarElemento :: String -> [String] -> [String]
sacarElemento cadena [] = []
sacarElemento cadena (x:xs) | cadena == x = sacarElemento cadena xs
                            | otherwise = x : sacarElemento cadena xs 

--Ejercicio 2
stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto [] nombre = 0
stockDeProducto ((producto, cantidad):xs) nombre | nombre == producto = cantidad
                                                 | otherwise = stockDeProducto xs nombre

--Ejecicio 3
dineroEnStock :: [(String, Int)]->[(String, Float)]->Float
dineroEnStock [] lista = 0
dineroEnStock (x:xs) lista = calcularDinero x lista + dineroEnStock xs lista 

calcularDinero :: (String, Int)->[(String, Float)]->Float
calcularDinero lista [] = 0
calcularDinero (nombre, cantidad) ((producto, precio):xs) | nombre == producto = fromIntegral(cantidad) * precio
                                                          | otherwise = calcularDinero (nombre,cantidad) xs

--Ejercicio 4
aplicarOferta :: [(String, Int)]->[(String, Float)]->[(String,Float)]
aplicarOferta stock [] = []
aplicarOferta stock ((producto, precio):xs) | (stockDeProducto stock producto) > 10 = (producto, precio*0.8) : aplicarOferta stock xs
                                            | otherwise = (producto, precio) : aplicarOferta stock xs