# forfiles

> Egy vagy több fájl kiválasztása egy megadott parancs végrehajtásához. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/forfiles>.

- Fájlok keresése az aktuális könyvtárban:

`forfiles`

- Egy adott könyvtárban lévő fájlok keresése:

`forfiles /p {{path/to/directory}}`

- A megadott parancs futtatása minden egyes fájlra:

`forfiles /c "{{command}}"`

- Fájlok keresése egy adott glob maszk segítségével:

`forfiles /m {{glob_pattern}}`

- Fájlok rekurzív keresése:

`forfiles /s`

- 5 napnál régebbi fájlok keresése:

`forfiles /d {{+5}}`
