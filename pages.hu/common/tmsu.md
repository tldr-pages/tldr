# tmsu

> Egyszerű parancssori eszköz fájlok címkézésére. További információ: <https://tmsu.org>.

- Egy adott fájl címkézése több címkével:

`tmsu tag {{path/to/file.mp3}} {{music}} {{big-jazz}} {{mp3}}`

- Több fájl címkézése:

`tmsu tag --tags "{{music mp3}}" {{*.mp3}}`

- Megadott fájl(ok) címkéinek listázása:

`tmsu tags {{*.mp3}}`

- Megadott címkével (címkékkel) rendelkező fájlok listázása:

`tmsu files {{big-jazz}} {{music}}`

- List files with tags matching boolean expression:

`tmsu files "{{(year >= 1990 and year <= 2000)}} and {{grunge}}"`

- A tmsu virtuális fájlrendszer csatlakoztatása egy meglévő könyvtárba:

`tmsu mount {{path/to/directory}}`
