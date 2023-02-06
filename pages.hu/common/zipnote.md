# zipnote

> A zip-archívum megjegyzéseinek megtekintése, hozzáadása vagy szerkesztése. A fájlok átnevezhetők a zip-archívumban. További információ: <https://manned.org/zipnote>.

- A zip-archívumok megjegyzéseinek megtekintése:

`zipnote {{path/to/file.zip}}`

- A zip-archívumhoz tartozó megjegyzések kivonása egy fájlba:

`zipnote {{path/to/file.zip}} > {{path/to/file.txt}}`

- Hozzáadhatja/frissítheti egy zip-archívum megjegyzéseit egy fájlból:

`zipnote -w {{path/to/file.zip}} < {{path/to/file.txt}}`
