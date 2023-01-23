# sqlite3

> Az SQLite 3 parancssori interfésze, amely egy önálló fájlalapú beágyazott SQL-motor. További információ: <https://sqlite.org>.

- Indítson el egy interaktív héjat egy új adatbázissal:

`sqlite3`

- Interaktív héj megnyitása egy meglévő adatbázis ellenében:

`sqlite3 {{path/to/database.sqlite3}}`

- SQL utasítás végrehajtása egy adatbázis ellen, majd kilépés:

`sqlite3 {{path/to/database.sqlite3}} '{{SELECT * FROM some_table;}}'`
