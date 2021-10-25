# pacman

> Arch Linux Paket Management Tool.
> Manche Unterbefehle wie `pacman sync` sind separat dokumentiert.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Synchronisiere und aktualisiere alle Pakete:

`sudo pacman --sync --refresh --sysupgrade`

- Installiere ein neues Paket:

`sudo pacman --sync {{paketname}}`

- Entferne ein Paket und dessen Abhängigkeiten:

`sudo pacman --remove --recursive {{paketname}}`

- Suche in der Paketdatenbank nach einem regulären Ausdruck oder Schlüsselwort:

`pacman --sync --search "{{suchmuster}}"`

- Liste alle installierten Pakete und dessen Versionen auf:

`pacman --query`

- Liste alle ausdrücklich installierten Pakete und dessen Versionen auf:

`pacman --query --explicit`

- Zeige verwaiste Pakete an, welche als Abhängigkeiten installiert wurden, aber nicht mehr von anderen Paketen benötigt werden.

`pacman --query --unrequired --deps --quiet`

- Leere den gesamten pacman Cache:

`sudo pacman --sync --clean --clean`
