# nodemon

> Fájlok figyelése és a csomóponti alkalmazás automatikus újraindítása, ha változásokat észlel. További információ: <https://nodemon.io>.

- A megadott fájl végrehajtása és egy adott fájl figyelése a változásokra:

`nodemon {{path/to/file.js}}`

- A nodemon manuális újraindítása (megjegyzés: a nodemon-nak már aktívnak kell lennie ahhoz, hogy ez működjön):

`rs`

- Meghatározott fájlok figyelmen kívül hagyása:

`nodemon --ignore {{path/to/file_or_directory}}`

- Érvek átadása a node alkalmazásnak:

`nodemon {{path/to/file.js}} {{arguments}}`

- Érvek átadása magának a node-nak, ha azok nem nodemon-argumentumok (pl. `--inspect`):

`nodemon {{arguments}} {{path/to/file.js}}`

- Egy tetszőleges, nem csomóponti szkript futtatása:

`nodemon --exec "{{command_to_run_script}} {{options}}" {{path/to/script}}`

- Python szkript futtatása:

`nodemon --exec "python {{options}}" {{path/to/file.py}}`
