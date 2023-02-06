# mysqld

> Indítsa el a MySQL adatbázis-kiszolgálót. További információ: <https://dev.mysql.com/doc/refman/en/mysqld.html>.

- Indítsa el a MySQL adatbázis-kiszolgálót:

`mysqld`

- Indítsa el a kiszolgálót, hibaüzeneteket nyomtatva a konzolra:

`mysqld --console`

- Indítsa el a kiszolgálót, a naplózási kimenetek mentése egy egyéni naplófájlba:

`mysqld --log={{path/to/file.log}}`

- Nyomtassa ki az alapértelmezett argumentumokat és azok értékeit, majd lépjen ki:

`mysqld --print-defaults`

- A kiszolgáló indítása, az argumentumok és értékek beolvasása egy fájlból:

`mysqld --defaults-file={{path/to/file}}`

- A kiszolgáló indítása és figyelése egy egyéni porton:

`mysqld --port={{port}}`

- Az összes súgóopció megjelenítése és kilépés:

`mysqld --verbose --help`
