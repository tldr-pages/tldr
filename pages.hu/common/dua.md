# dua

> A Dua (Disk Usage Analyzer) egy olyan eszköz, amellyel kényelmesen tájékozódhat egy adott könyvtár lemezterületének felhasználásáról. További információk: <https://github.com/Byron/dua-cli>.

- Konkrét könyvtár elemzése:

`dua {{path/to/directory}}`

- Lemezhasználat helyett a látszólagos méret megjelenítése:

`dua --apparent-size`

- Számolja meg a keményen összekapcsolt fájlokat minden egyes alkalommal, amikor megjelenik:

`dua --count-hard-links`

- Egy vagy több könyvtár vagy fájl elfogyasztott helyének összesítése:

`dua aggregate`

- A terminál felhasználói felületének elindítása:

`dua interactive`

- Bájtszámok nyomtatásának formázása:

`dua --format {{metric|binary|bytes|GB|GiB|MB|MiB}}`

- A használandó szálak számának beállítása:

`dua --threads {{count}}`
