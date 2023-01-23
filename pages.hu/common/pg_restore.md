# pg_restore

> PostgreSQL adatbázis visszaállítása a pg_dump által létrehozott archív fájlból. További információ: <https://www.postgresql.org/docs/current/app-pgrestore.html>.

- Archívum visszaállítása egy meglévő adatbázisba:

`pg_restore -d {{db_name}} {{archive_file.dump}}`

- Ugyanaz, mint a fentiekben, a felhasználónév testreszabása:

`pg_restore -U {{username}} -d {{db_name}} {{archive_file.dump}}`

- Ugyanaz, mint fent, testreszabott host és port:

`pg_restore -h {{host}} -p {{port}} -d {{db_name}} {{archive_file.dump}}`

- Az archívumban szereplő adatbázis-objektumok listázása:

`pg_restore --list {{archive_file.dump}}`

- Adatbázisobjektumok tisztítása létrehozásuk előtt:

`pg_restore --clean -d {{db_name}} {{archive_file.dump}}`

- Több feladat használata a visszaállításhoz:

`pg_restore -j {{2}} -d {{db_name}} {{archive_file.dump}}`
