# pacman --query

> Arch Linux Paket Management tool.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8.de>.

- Liste alle installierten Pakete und dessen Versionen auf:

`pacman --query`

- Liste alle ausdrücklich installierten Pakete und dessen Versionen auf:

`pacman --query --explicit`

- Finde heraus welches Paket eine Datei besitzt:

`pacman --query --owns {{dateiname}}`

- Zeige Informationen über ein installiertes Paket an:

`pacman --query --info {{paketname}}`

- Liste alle Dateien auf welche einem Paket gehören:

`pacman --query --list {{paketname}}`

- Liste verwaiste Pakete auf (Pakete welche als Abhängigkeit installiert wurden, aber von keinem Paket benötigt werden):

`pacman --query --unrequired --deps --quiet`

- Liste installierte Pakete auf welche nicht in den Repositorien gefunden werden können:

`pacman --query --foreign`

- Liste veraltete Pakete auf:

`pacman --query --upgrades`
