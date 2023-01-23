# inotifywait

> Vár egy vagy több fájl módosítására. További információ: <https://manned.org/inotifywait>.

- Figyeli egy adott fájl eseményeit, és az első esemény után kilép:

`inotifywait {{path/to/file}}`

- Folyamatosan figyeli egy adott fájl eseményeit kilépés nélkül:

`inotifywait --monitor {{path/to/file}}`

- Egy könyvtár rekurzív figyelése eseményekre:

`inotifywait --monitor --recursive {{path/to/directory}}`

- Egy könyvtár figyelése a változásokra, kivéve azokat a fájlokat, amelyek neve megfelel egy reguláris kifejezésnek:

`inotifywait --monitor --recursive --exclude "{{regular_expression}}" {{path/to/directory}}`

- Egy fájl figyelése változásokra, kilépve, ha 30 másodpercig nem történik esemény:

`inotifywait --monitor --timeout {{30}} {{path/to/file}}`

- Csak a fájl módosítási események figyelése:

`inotifywait --event {{modify}} {{path/to/file}}`

- Csak az eseményeket figyeli, állapotüzenetek nélkül:

`inotifywait --quiet {{path/to/file}}`

- Futtasson egy parancsot, amikor egy fájlhoz hozzáfér:

`inotifywait --event {{access}} {{path/to/file}} && {{command}}`
