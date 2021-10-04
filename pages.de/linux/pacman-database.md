# pacman --database

> Mit der Arch Linux Paketdatenbank arbeiten.
> Verschiedene Attribute von installierten Paketen bearbeiten.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8.de>.

- Hilfe anzeigen:

`pacman --database --help`

- Ein Paket als implizit installiert markieren:

`sudo pacman --database --asdeps {{paketname}}`

- Ein Paket als explizit installiert markieren:

`sudo pacman --database --asexplicit {{paketname}}`

- Überprüfen dass alle Paketabhängigkeiten installiert sind:

`pacman --database --check`

- In den Repositorien überprüfen, dass alle angegebenen Abhängigkeiten verfügbar sind:

`pacman --database --check --check`

- Nur Fehlermeldungen anzeigen:

`pacman --database --check --quiet`
