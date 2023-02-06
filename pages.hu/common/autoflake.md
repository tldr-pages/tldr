# autoflake

> Eszköz a Python kódból a nem használt importok és változók eltávolítására. További információ: <https://github.com/myint/autoflake>.

- A nem használt változók eltávolítása egyetlen fájlból és a diff megjelenítése:

`autoflake --remove-unused-variables {{file.py}}`

- A nem használt importok eltávolítása több fájlból és a diffek megjelenítése:

`autoflake --remove-all-unused-imports {{file1.py}} {{file2.py}} {{file3.py}}`

- Nem használt változók eltávolítása egy fájlból, a fájl felülírásával:

`autoflake --remove-unused-variables --in-place {{file.py}}`

- A nem használt változók rekurzív módon történő eltávolítása egy könyvtár összes fájljából, minden egyes fájl felülírásával:

`autoflake --remove-unused-variables --in-place --recursive {{path/to/directory}}`
