# mysql

> A MySQL parancssori eszköz. További információ: <https://www.mysql.com/>.

- Csatlakozás egy adatbázishoz:

`mysql {{database_name}}`

- Csatlakozás egy adatbázishoz, a felhasználónak jelszót kell megadnia:

`mysql -u {{user}} --password {{database_name}}`

- Csatlakozás egy másik állomáson lévő adatbázishoz:

`mysql -h {{database_host}} {{database_name}}`

- Csatlakozás egy adatbázishoz Unix socket-en keresztül:

`mysql --socket {{path/to/socket.sock}}`

- SQL utasítások végrehajtása egy szkriptfájlban (batch fájl):

`mysql -e "source {{filename.sql}}" {{database_name}}`

- Adatbázis visszaállítása a `mysqldump` segítségével készített biztonsági másolatból (a felhasználónak jelszót kell megadnia):

`mysql --user {{user}} --password {{database_name}} < {{path/to/backup.sql}}`

- Az összes adatbázis visszaállítása biztonsági másolatból (a felhasználónak jelszót kell megadnia):

`mysql --user {{user}} --password < {{path/to/backup.sql}}`
