# fuser

> A fájlokat vagy foglalatokat jelenleg használó folyamatok azonosítóinak megjelenítése. További információ: <https://manned.org/fuser>.

- Megtalálja, hogy mely folyamatok férnek hozzá egy fájlhoz vagy könyvtárhoz:

`fuser {{path/to/file_or_directory}}`

- További mezők megjelenítése (`USER`, `PID`, `ACCESS` és `COMMAND`):

`fuser --verbose {{path/to/file_or_directory}}`

- TCP foglalatot használó folyamatok azonosítása:

`fuser --namespace tcp {{port}}`

- A fájlhoz vagy könyvtárhoz hozzáférő összes folyamat megállítása (a `SIGKILL` jelet küldi):

`fuser --kill {{path/to/file_or_directory}}`

- Megkeresni, hogy mely folyamatok férnek hozzá egy adott fájlt vagy könyvtárat tartalmazó fájlrendszerhez:

`fuser --mount {{path/to/file_or_directory}}`

- Egy adott porton TCP-kapcsolattal rendelkező összes folyamat megállítása:

`fuser --kill {{port}}/tcp`
