# pg_dump

> A PostgreSQL adatbázis kivonatolása egy szkriptfájlba vagy más archív fájlba. További információ: <https://www.postgresql.org/docs/current/app-pgdump.html>.

- Adatbázis dumpolása egy SQL-script fájlba:

`pg_dump {{db_name}} > {{output_file.sql}}`

- Ugyanaz, mint a fentiekben, a felhasználónév testreszabása:

`pg_dump -U {{username}} {{db_name}} > {{output_file.sql}}`

- Ugyanaz, mint fent, testreszabott host és port:

`pg_dump -h {{host}} -p {{port}} {{db_name}} > {{output_file.sql}}`

- Adatbázis dumpolása egyéni formátumú archív fájlba:

`pg_dump -Fc {{db_name}} > {{output_file.dump}}`

- Csak az adatbázis adatainak dumpolása egy SQL-script fájlba:

`pg_dump -a {{db_name}} > {{path/to/output_file.sql}}`

- Csak séma (adatdefiníciók) dömperlése SQL-script fájlba:

`pg_dump -s {{db_name}} > {{path/to/output_file.sql}}`
