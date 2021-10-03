# pacman

> Arch Linux Paket Management Tool.
> Manche Unterbefehle wie `pacman sync` sind separat dokumentiert.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8.de>.

- Synchronisieren und alle Pakete aktualisieren:

`pacman --sync --refresh --sysupgrade`

- Ein neues Paket installieren:

`pacman --sync {{paket_name}}`

- Ein Paket und dessen Abhängigkeiten entfernen:

`pacman --remove --recursive {{paket_name}}`

- In der Paketdatenbank nach einem regulären Ausdruck oder Schlüsselwort suchen:

`pacman --sync --search "{{such_muster}}"`

- Installierte Pakete und dessen Versionen auflisten:

`pacman --query`

- Nur ausdrücklich installierte Pakete und dessen Versionen auflisten:

`pacman --query --explicit`

- Verwaiste Pakete anzeigen, die als Abhängigkeiten installiert wurden, aber nicht mehr von anderen Paketen benötigt werden.

`pacman --query --unrequired --deps --quiet`

- Gesamten pacman Cache leeren:

`pacman --sync --clean --clean`
