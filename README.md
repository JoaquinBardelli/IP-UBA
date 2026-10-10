# IP-UBA

Ejercicios y prácticas de **Introducción a la Programación** (UBA): guías prácticas y parciales resueltos en Haskell y Python.

## Estructura

```
haskell/
├── guias/       Guías 3 a 5 (+ tests de la guía 5 con HUnit)
└── parciales/   Simulacros, repasos y parciales anteriores
python/
└── guias/       Guías 6 a 8 (+ tests de la guía 7 con unittest)
```

| Guía | Lenguaje | Archivo |
|------|----------|---------|
| 3, 4, 5 | Haskell | `haskell/guias/GuiaN.hs` |
| 6, 7, 8 | Python | `python/guias/GuiaN.py` |

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

```bash
cd python/guias
python -m unittest testGuia7
```

## Estado

- [x] Guías 3–7
- [ ] Guía 8 (pilas terminadas, en curso)
