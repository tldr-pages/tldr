# psql

> PostgreSQL parancssori kliens. További információ: <https://www.postgresql.org/docs/current/app-psql.html>.

- Csatlakozás az adatbázishoz. Alapértelmezés szerint az 5432-es portot használó helyi foglalathoz csatlakozik az aktuálisan bejelentkezett felhasználóval:

`psql {{database}}`

- Csatlakozás az adott porton futó adott szerver hoszton lévő adatbázishoz adott felhasználónévvel, jelszókérés nélkül:

`psql -h {{host}} -p {{port}} -U {{username}} {{database}}`

- Csatlakozás az adatbázishoz; a felhasználónak jelszót kell kérnie:

`psql -h {{host}} -p {{port}} -U {{username}} -W {{database}}`

- Egyetlen SQL lekérdezés vagy PostgreSQL parancs végrehajtása az adott adatbázisban (hasznos a shell szkriptekben):

`psql -c '{{query}}' {{database}}`

- Parancsok végrehajtása egy fájlból az adott adatbázisban:

`psql {{database}} -f {{file.sql}}`
