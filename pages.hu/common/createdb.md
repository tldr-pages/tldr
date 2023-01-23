# createdb

> PostgreSQL adatbázis létrehozása. További információ: <https://www.postgresql.org/docs/current/app-createdb.html>.

- Hozzon létre egy adatbázist, amely az aktuális felhasználó tulajdonában van:

`createdb {{database_name}}`

- Egy adott felhasználó tulajdonában lévő adatbázis létrehozása egy leírással:

`createdb --owner={{username}} {{database_name}} '{{description}}'`

- Adatbázis létrehozása sablonból:

`createdb --template={{template_name}} {{database_name}}`
