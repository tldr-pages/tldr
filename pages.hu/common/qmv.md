# qmv

> Fájlok és könyvtárak áthelyezése az alapértelmezett szövegszerkesztővel a fájlnevek meghatározásához. További információ: <https://www.nongnu.org/renameutils/>.

- Egyetlen fájl áthelyezése (nyisson meg egy szerkesztőt, amelynek bal oldalán a forrásfájl neve, jobb oldalán pedig a célfájl neve szerepel):

`qmv {{source_file}}`

- Több JPG fájl áthelyezése:

`qmv {{*.jpg}}`

- Több könyvtár áthelyezése:

`qmv -d {{path/to/directory1}} {{path/to/directory2}} {{path/to/directory3}}`

- Az összes fájl és könyvtár áthelyezése egy könyvtáron belül:

`qmv --recursive {{path/to/directory}}`

- Fájlok áthelyezése, de a forrás- és a célfájlnév pozíciójának felcserélése a szerkesztőben:

`qmv --option swap {{*.jpg}}`

- Az aktuális könyvtárban lévő összes fájl és mappa átnevezése, de a szerkesztőben csak a célfájlnevek jelennek meg (egyfajta egyszerű módként is elképzelhető):

`qmv --format=do .`
