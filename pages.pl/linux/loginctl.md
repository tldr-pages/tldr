# loginctl

> Zarządzaj menedżerem logowania systemd.
> Więcej informacji: <https://www.freedesktop.org/software/systemd/man/loginctl.html>.

- Wyświetl wszystkie aktualne sesje:

`loginctl list-sessions`

- Wyświetl wszystkie właściwości podanej sesji:

`loginctl show-session {{id_sesji}} --all`

- Wyświetl wszystkie właściwości podanego użytkownika:

`loginctl show-user {{nazwa_użytkownika}}`

- Wyświetl podaną właściwość użytkownika:

`loginctl show-user {{nazwa_użytkownika}} --property={{nazwa_właściwości}}`

- Uruchom operację `loginctl` na zdalnym hoście:

`loginctl list-users -H {{nazwa_hosta}}`
