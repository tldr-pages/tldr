# prctl

> Pobieranie lub ustawianie kontroli zasobów uruchomionych procesów, zadań i projektów.
> Więcej informacji: <https://www.unix.com/man-page/sunos/1/prctl>.

- Sprawdzenie limitów procesów i uprawnień:

`prctl {{pid}}`

- Sprawdzenie limitów procesów i uprawnień w formacie przetwarzalnym przez maszynę:

`prctl -P {{pid}}`

- Uzyskanie określonego limitu dla uruchomionego procesu:

`prctl -n process.max-file-descriptor {{pid}}`
