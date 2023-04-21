# homectl

> Twórz, usuwaj, zmieniaj lub sprawdzaj katalogi domowe używając usługi systemd-homed.
> Więcej informacji: <https://manned.org/homectl>.

- Wyświetl konta użytkowników i ich powiązane katalogi domowe:

`homectl list`

- Utwórz konto użytkownika i jego powiązany katalog domowy:

`sudo homectl create {{nazwa_użytkownika}}`

- Usuń podanego użytkownika i jego powiązany katalog domowy:

`sudo homectl remove {{nazwa_użytkownika}}`

- Zmień hasło podanego użytkownika:

`sudo homectl passwd {{nazwa_użytkownika}}`

- Uruchom powłokę lub komendę z dostępem do podanego katalogu domowego:

`sudo homectl with {{nazwa_użytkownika}} -- {{komenda}} {{argumenty_dla_komendy}}`

- Zablokuj lub odblokuj podany katalog domowy:

`sudo homectl {{lock|unlock}} {{nazwa_użytkownika}}`

- Zmień miejsce na dysku przydzielone dla podanego katalogu domowego na 100 GiB:

`sudo homectl resize {{nazwa_użytkownika}} {{100G}}`

- Wyświetl pomoc:

`homectl --help`
