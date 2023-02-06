# pg_dumpall

> A PostgreSQL adatbázis-fürt kivonatolása egy szkriptfájlba vagy más archív fájlba. További információ: <https://www.postgresql.org/docs/current/app-pg-dumpall.html>.

- Az összes adatbázis kiürítése:

`pg_dumpall > {{path/to/file.sql}}`

- Az összes adatbázis kiürítése egy adott felhasználónévvel:

`pg_dumpall --username={{username}} > {{path/to/file.sql}}`

- Ugyanaz, mint a fentiekben, testreszabott host és port:

`pg_dumpall -h {{host}} -p {{port}} > {{output_file.sql}}`

- Az összes adatbázis dumpolása egy egyéni formátumú archív fájlba, mérsékelt tömörítéssel:

`pg_dumpall -Fc > {{output_file.dump}}`

- Csak az adatbázisok adatainak dumpolása egy SQL-szkriptfájlba:

`pg_dumpall --data-only > {{path/to/file.sql}}`

- Csak a séma (adatdefiníciók) dömperlése egy SQL-script fájlba:

`pg_dumpall -s > {{output_file.sql}}`
