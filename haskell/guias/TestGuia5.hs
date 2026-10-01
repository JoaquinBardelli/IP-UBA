module TestGuia5 where

import Test.HUnit
import Guia5 

runFibo :: IO Counts
runFibo = runTestTT testsFibo

testsFibo :: Test
testsFibo = test [
    "Caso base 1: fib 0" ~: fib 0 @?= 0,
    "Caso base 2: fib 1" ~: fib 1 @?= 1,
    "Caso recursivo: fib 2" ~: fib 2 @?= 1
]