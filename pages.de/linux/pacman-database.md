# pacman --database

> Mit der Arch Linux Paketdatenbank arbeiten.
> Verschiedene Attribute von installierten Paketen bearbeiten.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Zeige Hilfe an:

`pacman --database --help`

- Markiere ein Paket als implizit installiert:

`sudo pacman --database --asdeps {{paketname}}`

- Markiere ein Paket als explizit installiert:

`sudo pacman --database --asexplicit {{paketname}}`

- Überprüfe, dass alle Paketabhängigkeiten installiert sind:

`pacman --database --check`

- Überprüfe in den Repositorien, dass alle angegebenen Abhängigkeiten verfügbar sind:

`pacman --database --check --check`

- Zeige nur Fehlermeldungen:

`pacman --database --check --quiet`
