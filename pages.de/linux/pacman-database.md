# pacman --database

> Mit der Arch Linux Paketdatenbank arbeiten.
> Verschiedene Attribute von installierten Paketen bearbeiten.
> Siehe auch: `pacman`.
> Weitere Informationen: <https://manned.org/pacman.8>.

- Markiere ein Paket als implizit installiert:

`sudo pacman -D --asdeps {{paketname}}`

- Markiere ein Paket als explizit installiert:

`sudo pacman -D --asexplicit {{paketname}}`

- Überprüfe, dass alle Paketabhängigkeiten installiert sind:

`pacman -Dk`

- Überprüfe in den Repositorien, dass alle angegebenen Abhängigkeiten verfügbar sind:

`pacman -Dkk`

- Zeige nur Fehlermeldungen:

`pacman -Dkq`

- Zeige Hilfe an:

`pacman -Dh`
