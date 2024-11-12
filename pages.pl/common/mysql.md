# mysql

> Narzędzie wiersza polecenia MySQL.
> Więcej informacji: <https://www.mysql.com/>.

- Połącz się z bazą danych:

`mysql {{nazwa_bazy_danych}}`

- Połącz się z bazą danych, użytkownik zostanie poproszony o podanie hasła:

`mysql -u {{użytkownik}} --password {{nazwa_bazy_danych}}`

- Połącz się z bazą danych na innym hoście:

`mysql -h {{host_bazy_danych}} {{nazwa_bazy_danych}}`

- Połącz się z bazą danych przez gniazdo Unix:

`mysql --socket {{ścieżka/do/gniazda.sock}}`

- Wykonuj instrukcje SQL w pliku skryptu (plik wsadowy):

`mysql -e "source {{nazwa_pliku.sql}}" {{nazwa_bazy_danych}}`

- Przywróć bazę danych z kopii zapasowej (użytkownik zostanie poproszony o podanie hasła):

`mysql --user {{użytkownik}} --password {{nazwa_bazy_danych}} < {{ścieżka/do/kopii_zapasowej.sql}}`

- Przywróć wszystkie bazy danych z kopii zapasowej (użytkownik zostanie poproszony o podanie hasła):

`mysql --user {{użytkownik}} --password < {{ścieżka/do/kopii_zapasowej.sql}}`
