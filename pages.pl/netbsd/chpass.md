# chpass

> Dodaj lub zmień informacje w bazie danych użytkowników, w tym powłokę logowania i hasło.
> Zobacz także: `passwd`.
> Więcej informacji: <https://man.netbsd.org/chpass>.

- Ustaw określoną powłokę logowania dla bieżącego użytkownika w sposób interaktywny:

`su -c chpass`

- Ustaw określoną powłokę (z ang. [s]hell) logowania dla bieżącego użytkownika:

`chpass -s {{ścieżka/do/powłoki}}`

- Ustaw powłokę (z ang. [s]hell) logowania dla określonego użytkownika:

`chpass -s {{ścieżka/do/powłoki}} {{nazwa_użytkownika}}`

- Określ wpis bazy danych użytkownika w formacie pliku `passwd`:

`su -c 'chpass -a {{nazwa_użytkownika:zaszyfrowane_hasło:uid:gid:...}} -s {{ścieżka/do/pliku}}' {{nazwa_użytkownika}}`

- Aktualizuj tylko [l]okalny plik haseł:

`su -c 'chpass -l -s {{ścieżka/do/powłoki}}' {{nazwa_użytkownika}}`

- Wymuś zmianę wpisu w bazie danych [y]P haseł:

`su -c 'chpass -y -s {{ścieżka/do/powłoki}}' {{nazwa_użytkownika}}`
