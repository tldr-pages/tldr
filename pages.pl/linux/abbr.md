# abbr

> Zarządza skrótami dla powłoki fish.
> Zdefiniowane przez użytkownika słowa są zastępowane po wpisaniu dłuższymi zwrotami.
> Więcej informacji: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Dodanie nowego skrótu:

`abbr --add {{nazwa_skrótu}} {{polecenie}} {{argumenty_polecenia}}`

- Zmiana nazwy istniejącego skrótu:

`abbr --rename {{stara_nazwa}} {{nowa_nazwa}}`

- Usunięcie istniejącego skrótu:

`abbr --erase {{nazwa_skrótu}}`

- Import skrótów zdefiniowanych na innym hoście poprzez SSH:

`ssh {{nazwa_hosta}} abbr --show | source`
