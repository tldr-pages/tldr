# chpass

> Dodaj lub zmień informacje w bazie danych użytkowników, w tym powłokę logowania i hasło.
> Zobacz także: `passwd`.
> Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Dodaj lub zmień informacje w bazie danych użytkowników dla bieżącego użytkownika w sposób interaktywny:

`su -c chpass`

- Ustaw określoną powłokę (z ang. [s]hell) logowania dla bieżącego użytkownika:

`chpass -s {{ścieżka/do/powłoki}}`

- Ustaw powłokę (z ang. [s]hell) logowania dla określonego użytkownika:

`chpass -s {{ścieżka/do/powłoki}} {{nazwa_użytkownika}}`

- Zmień czas wygaśnięcia (z ang. [e]xpire) konta (w sekundach od daty początku epoki, UTC):

`su -c 'chpass -e {{czas}} {{nazwa_użytkownika}}'`

- Zmień hasło użytkownika:

`su -c 'chpass -p {{zaszyfrowane_hasło}} {{nazwa_użytkownika}}'`

- Określ nazwę [h]osta lub adres serwera NIS do zapytania:

`su -c 'chpass -h {{nazwa_hosta}} {{nazwa_użytkownika}}'`

- Określ konkretną [d]omenę NIS (domyślnie nazwa domeny systemowej):

`su -c 'chpass -d {{domain}} {{nazwa_użytkownika}}'`
