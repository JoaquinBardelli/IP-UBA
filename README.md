# IP-UBA

Ejercicios y prácticas de **Introducción a la Programación** (UBA): guías prácticas y parciales resueltos en Haskell y Python.

## Estructura

```
haskell/
├── guias/       Guías 3 a 5 (+ tests de la guía 5 con HUnit)
└── parciales/   Simulacros, repasos y parciales anteriores
python/
├── guias/
│   ├── Guia6.py
│   ├── Guia7/   Guía 7 completa + separada por tema (+ tests con unittest)
│   └── Guia8/   Guía 8 completa + separada por tema
└── parciales/   (vacía por ahora)
```

| Guía | Lenguaje | Archivo |
|------|----------|---------|
| 3, 4, 5 | Haskell | `haskell/guias/GuiaN.hs` |
| 6 | Python | `python/guias/Guia6.py` |
| 7 | Python | `python/guias/Guia7/` |
| 8 | Python | `python/guias/Guia8/` |

En las guías 7 y 8, `GuiaN.py` tiene la guía entera y los demás archivos son la misma guía separada por tema:

- **Guía 7:** `Busqueda.py` (recorrido y búsqueda en secuencias), `Filtrado.py` (filtrar, modificar y procesar secuencias), `Matrices.py`, `Interactivos.py` (programas interactivos)
- **Guía 8:** `Pilas.py`, `Colas.py`, `Diccionarios.py`

Parciales en `haskell/parciales/`: `parcial2024`, `SimulacroHaskell` (consigna en `consignaSimulacro.txt`), `Repaso`, `democracia`, `perfectosAmigos`, `sistemaStock`, `sopaDeNumeros`.

## Cómo correrlo

### Haskell

Requiere [GHC](https://www.haskell.org/ghcup/) y el paquete `HUnit` para los tests.

```bash
cd haskell/guias
ghci TestGuia5.hs
```

Dentro de GHCi, correr por ejemplo `runFibo`.

### Python

Requiere Python 3.

Los tests de la guía 7 se corren desde la raíz del repo:

```bash
python -m unittest python.guias.Guia7.testGuia7
```

`Guia7.py` termina con un programa interactivo (`historialMonedero`), así que al correr los tests pide una operación: escribir `X` para salir.

Los archivos por tema se corren desde su carpeta, porque algunos importan funciones de otros (por ejemplo, `Matrices.py` usa `ordenados` de `Busqueda.py`).

## Estado

- [x] Guías 3–7
- [ ] Guía 8 (pilas, colas y diccionarios terminados, en curso)
