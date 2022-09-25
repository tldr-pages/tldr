# pacman

> Arch Linux Paket Management Tool.
> Manche Unterbefehle wie `pacman sync` sind separat dokumentiert.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Synchronisiere und aktualisiere alle Pakete:

`sudo pacman -Syu`

- Installiere ein neues Paket:

`sudo pacman -S {{paketname}}`

- Entferne ein Paket und dessen Abhängigkeiten:

`sudo pacman -Rs {{paketname}}`

- Suche in der Paketdatenbank nach einem regulären Ausdruck oder Schlüsselwort:

`pacman -Ss "{{suchmuster}}"`

- Liste alle installierten Pakete und dessen Versionen auf:

`pacman -Q`

- Liste alle ausdrücklich installierten Pakete und dessen Versionen auf:

`pacman -Qe`

- Zeige verwaiste Pakete an, welche als Abhängigkeiten installiert wurden, aber nicht mehr von anderen Paketen benötigt werden.

`pacman -Qtdq`

- Leere den gesamten pacman Cache:

`sudo pacman -Scc`
