# pacman

> Arch Linux Paket Management Tool.
> Siehe auch: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Synchronisiere und aktualisiere alle Pakete:

`sudo pacman -Syu`

- Installiere ein neues Paket:

`sudo pacman -S {{paket}}`

- Entferne ein Paket und dessen Abhängigkeiten:

`sudo pacman -Rs {{paket}}`

- Liste alle installierten Pakete und dessen Versionen auf:

`pacman -Q`

- Liste alle ausdrücklich installierten Pakete und dessen Versionen auf:

`pacman -Qe`

- Zeige verwaiste Pakete an, welche als Abhängigkeiten installiert wurden, aber nicht mehr von anderen Paketen benötigt werden:

`pacman -Qtdq`

- Leere den gesamten pacman Cache:

`sudo pacman -Scc`
