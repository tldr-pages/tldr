# mongorestore

> Segédprogram gyűjtemény vagy adatbázis importálására bináris dumpból egy MongoDB példányba. További információ: <https://docs.mongodb.com/database-tools/mongorestore/>.

- BSON-adatdömping importálása egy könyvtárból egy MongoDB adatbázisba:

`mongorestore --db {{database_name}} {{path/to/directory}}`

- BSON-adatdömping importálása egy könyvtárból egy adott adatbázisba egy adott porton futó MongoDB szerver hoszton, felhasználói hitelesítéssel (a felhasználónak jelszót kell kérnie):

`mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/directory}} --password`

- Gyűjtemény importálása egy BSON fájlból egy MongoDB adatbázisba:

`mongorestore --db {{database_name}} {{path/to/file}}`

- Gyűjtemény importálása egy BSON fájlból egy adott adatbázisba egy adott porton futó MongoDB szerver hoszton, felhasználói hitelesítéssel (a felhasználónak jelszót kell kérnie):

`mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/file}} --password`
