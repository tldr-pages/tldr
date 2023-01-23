# autopep8

> Python kód formázása a PEP 8 stílus útmutató szerint. További információ: <https://github.com/hhatto/autopep8>.

- Egy fájl formázása a `stdout` címre, egyéni maximális sorhosszúsággal:

`autopep8 {{path/to/file.py}} --max-line-length {{length}}`

- Egy fájl formázása, a változtatások diff-jének megjelenítésével:

`autopep8 --diff {{path/to/file}}`

- Egy fájl helyben történő formázása és a változások mentése:

`autopep8 --in-place {{path/to/file.py}}`

- Egy könyvtárban lévő összes fájl rekurzív formázása helyben, és a változások mentése:

`autopep8 --in-place --recursive {{path/to/directory}}`
