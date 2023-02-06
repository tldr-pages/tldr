# pyflakes

> A Python forráskódfájlok hibaellenőrzése. További információ: <https://pypi.org/project/pyflakes>.

- Egyetlen Python fájl ellenőrzése:

`pyflakes check {{path/to/file}}.py`

- Egy adott könyvtárban lévő Python fájlok ellenőrzése:

`pyflakes checkPath {{path/to/directory}}`

- Egy könyvtárban lévő Python fájlok rekurzív ellenőrzése:

`pyflakes checkRecursive {{path/to/directory}}`

- Több könyvtárban található összes Python fájl ellenőrzése:

`pyflakes iterSourceCode {{path/to/directory_1}} {{path/to/directory_2}}`
