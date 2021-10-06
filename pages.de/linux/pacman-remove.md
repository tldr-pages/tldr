# pacman --remove

> Arch Linux Paketverwaltungs-Werkzeug.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Zeige Hilfe für diesen Unterbefehl an:

`pacman --remove --help`

- Entferne ein Paket und dessen Abhängigkeiten:

`sudo pacman --remove --recursive {{paketname}}`

- Entferne ein Paket sowie alle Abhängigkeiten und Konfigurationsdateien:

`sudo pacman --remove --recursive --nosave {{paketname}}`

- Entferne ein Paket ohne Bestätigungsaufforderung:

`sudo pacman --remove --noconfirm {{paketname}}`

- Entferne verwaiste Pakete (Pakete welche als Abhängigkeit installiert wurden, aber von keinem Paket benötigt werden):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Entferne ein Paket und alle Pakete die davon abhängig sind:

`sudo pacman --remove --cascade {{paketname}}`

- Liste Pakete auf, welche betroffen sein würden (entfernt keine Pakete):

`pacman --remove --print {{paketname}}`
