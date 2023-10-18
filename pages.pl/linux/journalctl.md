# journalctl

> Przeszukaj dziennik systemd.
> Więcej informacji: <https://manned.org/journalctl>.

- Wyświetl wszystkie wiadomości o priorytecie 3 (błędy) z tego rozruchu:

`journalctl -b --priority={{3}}`

- Wyświetl wszystkie wiadomości z ostatniego rozruchu:

`journalctl -b -1`

- Usuń dzienniki starsze niż 2 dni:

`journalctl --vacuum-time={{2d}}`

- Wyświetlaj nowe wiadomości (jak `tail -f` dla tradycyjnego sysloga):

`journalctl -f`

- Pokaż wszystkie wiadomości podanej jednostki:

`journalctl -u {{jednostka}}`

- Filtruj wiadomości w zakresie czasu (znacznik czasu lub symbol zastępczy, np. "yesterday"):

`journalctl --since {{now|today|yesterday|tomorrow}} --until {{YYYY-MM-DD HH:MM:SS}}`

- Wyświetl wszystkie wiadomości podanego procesu:

`journalctl _PID={{pid}}`

- Wyświetl wszystkie wiadomości podanego pliku wykonywalnego:

`journalctl {{ścieżka/do/pliku}}`
