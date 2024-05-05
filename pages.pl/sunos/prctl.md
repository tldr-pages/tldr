# prctl

> Pobieraj lub ustawiaj kontrolę zasobów uruchomionych procesów, zadań i projektów.
> Więcej informacji: <https://www.unix.com/man-page/sunos/1/prctl>.

- Sprawdż limity procesów i uprawnienia:

`prctl {{pid}}`

- Sprawdź limity procesów i uprawnienia w formacie przetwarzalnym przez maszynę:

`prctl -P {{pid}}`

- Uzyskaj określony limit dla uruchomionego procesu:

`prctl -n process.max-file-descriptor {{pid}}`
