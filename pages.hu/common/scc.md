# scc

> Go nyelven írt eszköz, amely megszámolja a kódsorokat. További információ: <https://github.com/boyter/scc>.

- Az aktuális könyvtárban lévő kódsorok kiírása:

`scc`

- A célkönyvtárban lévő kódsorok nyomtatása:

`scc {{path/to/directory}}`

- Kimenet megjelenítése minden fájlhoz:

`scc --by-file`

- Kimenet megjelenítése egy adott kimeneti formátummal (alapértelmezett: `tabular`):

`scc --format {{tabular|wide|json|csv|cloc-yaml|html|html-table}}`

- Csak a meghatározott fájlkiterjesztésű fájlokat számolja:

`scc --include-ext {{go, java, js}}`

- Könyvtárak kizárása a számlálásból:

`scc --exclude-dir {{.git,.hg}}`

- Kimenet megjelenítése és oszlopok szerinti rendezés (alapértelmezett beállítás: fájlok szerint):

`scc --sort {{files|name|lines|blanks|code|comments|complexity}}`

- Súgó nyomtatása az scc-hez:

`scc -h`
