# abbr

> Zarządzaj skrótami dla powłoki fish.
> Zdefiniowane przez użytkownika słowa są zastępowane po wpisaniu dłuższymi zwrotami.
> Więcej informacji: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Dodaj nowy skrót:

`abbr --add {{nazwa_skrótu}} {{polecenie}} {{argumenty_polecenia}}`

- Zmień nazwę istniejącego skrótu:

`abbr --rename {{stara_nazwa}} {{nowa_nazwa}}`

- Usuń istniejący skrót:

`abbr --erase {{nazwa_skrótu}}`

- Zaimportuj skróty zdefiniowane na innym hoście poprzez SSH:

`ssh {{nazwa_hosta}} abbr --show | source`
