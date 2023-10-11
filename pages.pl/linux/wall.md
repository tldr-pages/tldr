# wall

> Pisze wiadomość na terminalach aktualnie zalogowanych użytkowników.
> Więcej informacji: <https://manned.org/wall>.

- Wysłanie wiadomości:

`echo "{{wiadomość}}" | wall`

- Wysłanie wiadomoci z pliku:

`wall {{plik}}`

- Wysłanie wiadomość z pliku z podanym timeoutem (sekundy, domyślnie 300):

`wall -t {{sekundy}} {{plik}}`
