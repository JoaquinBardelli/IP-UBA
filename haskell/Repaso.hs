import Test.HUnit

generarStock :: [String] -> [(String, Int)]
generarStock [] = []
generarStock (x:xs) = (x,cantidadVeces x (x:xs)): generarStock (sacarTodos x xs) 

cantidadVeces :: String -> [String] -> Int
cantidadVeces item [] = 0
cantidadVeces item (x:xs) | item == x = 1 + cantidadVeces item xs
                          | otherwise = cantidadVeces item xs

sacarTodos :: String -> [String] -> [String]
sacarTodos item [] = []
sacarTodos item (x:xs) | item == x = sacarTodos item xs
                       | otherwise = x : sacarTodos item xs
                       

runStock :: IO Counts
runStock = runTestTT testStock

testStock :: Test
testStock = test [
    "Caso base: lista vacia []" ~: generarStock [] @?= [],
    "Caso varios distintos: [\"clavo\", \"tuerca\", \"tornillo\"]" ~: generarStock ["clavo", "tuerca", "tornillo"] @?= [("clavo",1),("tuerca",1),("tornillo",1)],
    "Un solo elemento repetido: [\"clavo\", \"clavo\", \"clavo\", \"clavo\"]" ~: generarStock ["clavo", "clavo", "clavo", "clavo"] @?= [("clavo", 4)],
    "Varios con repeticiones, ordenado: [\"clavo\", \"clavo\", \"clavo\", \"tuerca\", \"tuerca\"]" ~: generarStock ["clavo", "clavo", "clavo", "tuerca", "tuerca"] @?= [("clavo", 3), ("tuerca", 2)],
    "Varios con repeticiones, desordenado: [\"clavo\", \"tuerca\", \"tornillo\", \"clavo\", \"clavo\", \"tuerca\"]" ~: generarStock ["clavo", "tuerca", "tornillo", "clavo", "clavo", "tuerca"] @?= [("clavo", 3), ("tuerca", 2), ("tornillo", 1)],
    "Caso con mayúsculas mixtas: [\"Clavo\", \"clavo\", \"TUERCA\"]" ~: generarStock ["Clavo", "clavo", "TUERCA"] @?= [("clavo", 2), ("tuerca", 1)]
  ]