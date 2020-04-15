# mysql

> Narzędzie wiersza polecenia MySQL.
> Więcej informacji: <https://www.mysql.com/>.

- Połącz z bazą danych:

`mysql {{database_name}}`

- Połącz się z bazą danych, użytkownik zostanie poproszony o podanie hasła:

`mysql -u {{user}} --password {{database_name}}`

- Połącz się z bazą danych na innym hoście:

`mysql -h {{database_host}} {{database_name}}`

- Połącz się z bazą danych przez gniazdo Unix:

`mysql --socket {{path/to/socket.sock}}`

- Wykonuj instrukcje SQL w pliku skryptu (plik wsadowy):

`mysql -e "source {{filename.sql}}" {{database_name}}`

- Przywróć bazę danych z kopii zapasowej (użytkownik zostanie poproszony o podanie hasła):

`mysql --user {{user}} --password {{database_name}} < {{path/to/backup.sql}}`

- Przywróć wszystkie bazy danych z kopii zapasowej (użytkownik zostanie poproszony o podanie hasła):

`mysql --user {{user}} --password < {{path/to/backup.sql}}`
