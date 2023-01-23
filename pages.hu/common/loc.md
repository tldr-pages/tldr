# loc

> Rust nyelven írt eszköz, amely számolja a kódsorokat. További információ: <https://github.com/cgag/loc>.

- Kinyomtatja az aktuális könyvtárban található kódsorokat:

`loc`

- A célkönyvtárban lévő kódsorok nyomtatása:

`loc {{path/to/directory}}`

- Kódsorok nyomtatása statisztikákkal az egyes fájlokra:

`loc --files`

- Kódsorok nyomtatása .gitignore (stb.) fájlok nélkül (pl. két -u flaggel a rejtett fájlokat és könyvtárakat is megszámolja):

`loc -u`
