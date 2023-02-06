# mate-search-tool

> Fájlok keresése a MATE asztali környezetben. További információ: <https://manned.org/mate-search-tool>.

- Olyan fájlok keresése egy adott könyvtárban, amelyek egy adott karakterláncot tartalmaznak a nevükben:

`mate-search-tool --named={{string}} --path={{path/to/directory}}`

- Fájlok keresése a felhasználó megerősítésének megvárása nélkül:

`mate-search-tool --start --named={{string}} --path={{path/to/directory}}`

- Olyan fájlok keresése, amelyek neve megfelel egy adott reguláris kifejezésnek:

`mate-search-tool --start --regex={{string}} --path={{path/to/directory}}`

- Rendezési sorrend beállítása a keresési eredményekben:

`mate-search-tool --start --named={{string}} --path={{path/to/directory}} --sortby={{name|folder|size|type|date}}`

- Csökkenő rendezési sorrend beállítása:

`mate-search-tool --start --named={{string}} --path={{path/to/directory}} --descending`

- Egy adott felhasználó/csoport tulajdonában lévő fájlok keresése:

`mate-search-tool --start --{{user|group}}={{value}} --path={{path/to/directory}}`
