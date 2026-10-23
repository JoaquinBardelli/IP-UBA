<div align="center">

# 🎓 IP-UBA

**Ejercicios resueltos de Introducción a la Programación — UBA**

Guías prácticas y parciales resueltos en Haskell y Python.

![Haskell](https://img.shields.io/badge/Haskell-5D4F85?style=for-the-badge&logo=haskell&logoColor=white)
![Python](https://img.shields.io/badge/Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Guías](https://img.shields.io/badge/guías-3_a_8-2ea44f?style=for-the-badge)

</div>

---

## 📚 Contenido

| Guía | Lenguaje | Ubicación | Estado |
|:----:|:--------:|-----------|:------:|
| 3 | 🟣 Haskell | [`haskell/guias/Guia3.hs`](haskell/guias/Guia3.hs) | ✅ |
| 4 | 🟣 Haskell | [`haskell/guias/Guia4.hs`](haskell/guias/Guia4.hs) | ✅ |
| 5 | 🟣 Haskell | [`haskell/guias/Guia5.hs`](haskell/guias/Guia5.hs) + tests | ✅ |
| 6 | 🔵 Python | [`python/guias/Guia6.py`](python/guias/Guia6.py) | ✅ |
| 7 | 🔵 Python | [`python/guias/Guia7/`](python/guias/Guia7) + tests | ✅ |
| 8 | 🔵 Python | [`python/guias/Guia8/`](python/guias/Guia8) | ✅ |

### 🧩 Guías separadas por tema

En las guías 7 y 8, `GuiaN.py` tiene la guía **entera**, y además está separada en un archivo por tema:

<table>
<tr>
<th>📗 Guía 7</th>
<th>📘 Guía 8</th>
</tr>
<tr>
<td valign="top">

| Archivo | Tema |
|---------|------|
| `Busqueda.py` | Recorrido y búsqueda en secuencias |
| `Filtrado.py` | Filtrar, modificar y procesar secuencias |
| `Matrices.py` | Matrices |
| `Interactivos.py` | Programas interactivos |

</td>
<td valign="top">

| Archivo | Tema |
|---------|------|
| `Pilas.py` | Pilas (`LifoQueue`) |
| `Colas.py` | Colas (`Queue`) |
| `Diccionarios.py` | Diccionarios |
| `Archivos.py` | Lectura y escritura de archivos |

</td>
</tr>
</table>

> [!NOTE]
> `Archivos.py` trabaja con los `.txt` de su misma carpeta (`prueba.txt`, `notas.txt`, etc.), y algunos ejercicios escriben archivos de salida ahí.

### 📝 Parciales

Todos en [`haskell/parciales/`](haskell/parciales):

| Archivo | Descripción |
|---------|-------------|
| `parcial2024.hs` | Parcial 2024 |
| `SimulacroHaskell.hs` | Simulacro (consigna en `consignaSimulacro.txt`) |
| `Repaso.hs` | Repaso |
| `democracia.hs` · `perfectosAmigos.hs` · `sistemaStock.hs` · `sopaDeNumeros.hs` | Ejercicios tipo parcial |

`python/parciales/` está reservada para los parciales de Python (vacía por ahora).

---

## 🗂️ Estructura

```
IP-UBA/
├── haskell/
│   ├── guias/          Guías 3 a 5 (+ tests de la guía 5 con HUnit)
│   └── parciales/      Simulacros, repasos y parciales anteriores
└── python/
    ├── guias/
    │   ├── Guia6.py
    │   ├── Guia7/      Guía 7 completa + separada por tema (+ tests)
    │   └── Guia8/      Guía 8 completa + separada por tema
    └── parciales/      (vacía por ahora)
```

---

## ▶️ Cómo correrlo

<details>
<summary><b>🟣 Haskell</b></summary>

<br>

Requiere [GHC](https://www.haskell.org/ghcup/) y el paquete `HUnit` para los tests.

```bash
cd haskell/guias
ghci TestGuia5.hs
```

Dentro de GHCi, correr por ejemplo `runFibo`.

</details>

<details>
<summary><b>🔵 Python</b></summary>

<br>

Requiere Python 3.

Los tests de la guía 7 se corren desde la raíz del repo:

```bash
python -m unittest python.guias.Guia7.testGuia7
```

> [!TIP]
> `Guia7.py` termina con un programa interactivo (`historialMonedero`), así que al correr los tests pide una operación: escribí `X` para salir.

Los archivos por tema se corren **desde su carpeta**, porque algunos importan funciones de otros (por ejemplo, `Matrices.py` usa `ordenados` de `Busqueda.py`).

</details>

---

## ✅ Progreso

- [x] Guía 3
- [x] Guía 4
- [x] Guía 5
- [x] Guía 6
- [x] Guía 7
- [x] Guía 8 — pilas, colas, diccionarios y archivos
