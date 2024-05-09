# chpass

> Dodaj lub zmień informacje o użytkowniku w bazie danych, w tym powłoki logowania i hasła.
> Zobacz także: `passwd`.
> Więcej informacji: <https://man.openbsd.org/chsh>.

- Interaktywnie ustaw określoną powłokę logowania dla bieżącego użytkownika:

`doas chsh`

- Ustaw określoną powłokę (z ang. [s]hell) logowania dla bieżącego użytkownika:

`doas chsh -s {{ścieżka/do/powłoki}}`

- Ustaw określoną powłokę (z ang. [s]hell) logowania dla określonego użytkownika:

`doas chsh -s {{ścieżka/do/powłoki}} {{nazwa_użytkownika}}`

- Określ wpis bazy danych użytkownika w formacie pliku `passwd`:

`doas chsh -a {{nazwa_użytkownika:zaszyfrowane_hasło:uid:gid:...}}`
