# flake8

> A Python kód stílusának és minőségének ellenőrzésére szolgáló eszköz. További információ: <https://flake8.pycqa.org/>.

- Fájl vagy könyvtár rekurzívan történő futtatása:

`flake8 {{path/to/file_or_directory}}`

- Lint egy fájl vagy könyvtár rekurzívan, és megmutatja az egyes hibák sorát:

`flake8 --show-source {{path/to/file_or_directory}}`

- Lint egy fájl vagy könyvtár rekurzívan, és figyelmen kívül hagyja a szabályok listáját. (Az összes elérhető szabály megtalálható a flake8rules.com oldalon):

`flake8 --ignore {{rule1,rule2}} {{path/to/file_or_directory}}`

- Egy fájl vagy könyvtár rekurzív futtatása, de kizárja a megadott globs vagy alszövegek szerinti fájlokat:

`flake8 --exclude {{substring1,glob2}} {{path/to/file_or_directory}}`
