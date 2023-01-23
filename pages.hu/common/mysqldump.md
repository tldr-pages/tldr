# mysqldump

> Biztonsági mentés a MySQL-adatbázisokról. Lásd még: `mysql` az adatbázisok visszaállításához. További információ: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Biztonsági mentés létrehozása (a felhasználónak jelszót kell megadnia):

`mysqldump --user {{user}} --password {{database_name}} --result-file={{path/to/file.sql}}`

- Biztonsági mentés egy adott táblázatról, a kimenet átirányítása egy fájlba (a felhasználót jelszó megadására kéri):

`mysqldump --user {{user}} --password {{database_name}} {{table_name}} > {{path/to/file.sql}}`

- Biztonsági mentés az összes adatbázisról, a kimenetet egy fájlba irányítja át (a felhasználót jelszó megadására kéri):

`mysqldump --user {{user}} --password --all-databases > {{path/to/file.sql}}`

- Az összes adatbázis biztonsági mentése egy távoli állomásról, a kimenet átirányítása egy fájlba (a felhasználót jelszó megadására kéri):

`mysqldump --host={{ip_or_hostname}} --user {{user}} --password --all-databases > {{path/to/file.sql}}`
