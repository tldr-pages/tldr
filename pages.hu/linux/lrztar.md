# lrztar

> A `lrzip` csomagolása a könyvtárak tömörítésének egyszerűsítésére. Lásd még: `tar` `lrzuntar` `lrunzip` További információ: <https://manned.org/lrztar>.

- Archiváljon egy könyvtárat a `tar`, majd tömörítse:

`lrztar {{path/to/directory}}`

- Ugyanaz, mint fent, ZPAQ-val - extrém tömörítés, de nagyon lassú:

`lrztar -z {{path/to/directory}}`

- Adja meg a kimeneti fájlt:

`lrztar -o {{path/to/file}} {{path/to/directory}}`

- Felülbírálja a használni kívánt processzorszálak számát:

`lrztar -p {{8}} {{path/to/directory}}`

- A meglévő fájlok felülírásának kikényszerítése:

`lrztar -f {{path/to/directory}}`
