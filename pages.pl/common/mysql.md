# mysql

> Narzędzie wiersza polecenia MySQL.
> Więcej informacji: <https://www.mysql.com/>.

- Połącz z bazą danych:

`mysql {{nazwa_bazydanych}}`

- Połącz się z bazą danych, użytkownik zostanie poproszony o podanie hasła:

`mysql -u {{uzytkownik}} --password {{nazwa_bazydanych}}`

- Połącz się z bazą danych na innym hoście:

`mysql -h {{host_bazydanych}} {{nazwa_bazydanych}}`

- Połącz się z bazą danych przez gniazdo Unix:

`mysql --socket {{sciezka/do/socket.sock}}`

- Wykonuj instrukcje SQL w pliku skryptu (plik wsadowy):

`mysql -e "source {{nazwapliku.sql}}" {{nazwa_bazydanych}}`

- Przywróć bazę danych z kopii zapasowej (użytkownik zostanie poproszony o podanie hasła):

`mysql --user {{uzytkownik}} --password {{nazwa_bazydanych}} < {{sciezka/do/backup.sql}}`

- Przywróć wszystkie bazy danych z kopii zapasowej (użytkownik zostanie poproszony o podanie hasła):

`mysql --user {{uzytkownik}} --password < {{sciezka/do/backup.sql}}`
