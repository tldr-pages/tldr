# chpass

> Dodawanie lub zmiana informacji o użytkowniku w bazie danych, w tym powłoki logowania i hasła.
> Zobacz także: `passwd`.
> Więcej informacji: <https://man.openbsd.org/chsh>.

- Interaktywnie ustaw określoną powłokę logowania dla bieżącego użytkownika:

`doas chsh`

- Ustaw określoną powłokę (z ang. [s]hell) logowania dla bieżącego użytkownika:

`doas chsh -s {{sciezka/do/powloki}}`

- Ustawia określoną powłokę (z ang. [s]hell) logowania dla określonego użytkownika:

`doas chsh -s {{sciezka/do/powloki}} {{nazwa_uzytkownika}}`

- Określa wpis bazy danych użytkownika w formacie pliku `passwd`:

`doas chsh -a {{nazwa_uzytkownika:zaszyfrowane_haslo:uid:gid:...}}`
