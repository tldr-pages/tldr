# engrampa

> Fájlok csomagolása zip/tar fájlba a MATE asztali környezetben. Lásd még: `zip`, `tar`. További információ: [https://github.com/mate-desktop/engrampa.](https://github.com/mate-desktop/engrampa)

- Indítsa el az engrampa programot:

`engrampa`

- Meghatározott archívumok megnyitása:

`engrampa {{path/to/archive1.tar path/to/archive2.tar ...}}`

- Adott fájlok és/vagy könyvtárak rekurzív archiválása:

`engrampa --add-to={{path/to/compressed.tar}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Fájlok és/vagy könyvtárak kivonása archívumokból egy adott elérési útvonalra:

`engrampa --extract-to={{path/to/directory}} {{path/to/archive1.tar path/to/archive2.tar ...}}`
