# mongodump

> Segédprogram egy MongoDB példány tartalmának exportálásához. További információ: <https://docs.mongodb.com/database-tools/mongodump/>.

- Készítsen egy dumpot az összes adatbázisból (ez a fájlokat egy "dump" nevű könyvtárba helyezi):

`mongodump`

- Adja meg a dump kimeneti helyét:

`mongodump --out {{path/to/directory}}`

- Egy adott adatbázis dumpjának létrehozása:

`mongodump --db {{database_name}}`

- Egy adott adatbázis egy adott gyűjteményének dumpjának létrehozása:

`mongodump --collection {{collection_name}} --db {{database_name}}`

- Csatlakozás egy adott porton futó adott állomáshoz, és dump létrehozása:

`mongodump --host {{host}} --port {{port}}`

- Egy adott adatbázis dumpjának létrehozása egy adott felhasználónévvel; a felhasználónak jelszót kell kérnie:

`mongodump --username {{username}} {{database}} --password`

- Dump létrehozása egy adott példányból; a hoszt, a felhasználó, a jelszó és az adatbázis a csatlakozási karakterláncban lesz megadva:

`mongodump --uri {{connection_string}}`
