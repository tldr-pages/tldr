# mysql

> Narzędzie wiersza polecenia MySQL.
> Więcej informacji: <https://manned.org/mysql>.

- Połącz się z bazą danych:

`mysql {{nazwa_bazy_danych}}`

- Połącz się z bazą danych, użytkownik zostanie poproszony o podanie hasła:

`mysql {{[-u|--user]}} {{użytkownik}} {{[-p|--password]}} {{nazwa_bazy_danych}}`

- Połącz się z bazą danych na innym hoście:

`mysql {{[-h|--host]}} {{host_bazy_danych}} {{nazwa_bazy_danych}}`

- Połącz się z bazą danych przez gniazdo Unix:

`mysql {{[-S|--socket]}} {{ścieżka/do/gniazda.sock}}`

- Wykonuj instrukcje SQL w pliku skryptu (plik wsadowy):

`mysql {{[-e|--execute]}} "source {{nazwa_pliku.sql}}" {{nazwa_bazy_danych}}`

- Przywróć bazę danych z kopii zapasowej (użytkownik zostanie poproszony o podanie hasła):

`mysql {{[-u|--user]}} {{użytkownik}} {{[-p|--password]}} {{nazwa_bazy_danych}} < {{ścieżka/do/kopii_zapasowej.sql}}`

- Przywróć wszystkie bazy danych z kopii zapasowej (użytkownik zostanie poproszony o podanie hasła):

`mysql {{[-u|--user]}} {{użytkownik}} {{[-p|--password]}} < {{ścieżka/do/kopii_zapasowej.sql}}`
