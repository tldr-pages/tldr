# pacman --remove

> Arch Linux Paketverwaltungs-Werkzeug.
> Weitere Informationen: <https://manned.org/pacman.8>.

- Entferne ein Paket und dessen Abhängigkeiten:

`sudo pacman -Rs {{paket}}`

- Entferne ein Paket sowie alle Abhängigkeiten und Konfigurationsdateien:

`sudo pacman -Rsn {{paket}}`

- Entferne ein Paket ohne Bestätigungsaufforderung:

`sudo pacman -R --noconfirm {{paket}}`

- Entferne verwaiste Pakete (Pakete welche als Abhängigkeit installiert wurden, aber von keinem Paket benötigt werden):

`sudo pacman -Rsn $(pacman -Qdtq)`

- Entferne ein Paket und alle Pakete die davon abhängig sind:

`sudo pacman -Rc {{paket}}`

- Liste Pakete auf, welche betroffen sein würden (entfernt keine Pakete):

`pacman -Rp {{paket}}`

- Zeige Hilfe für diesen Unterbefehl an:

`pacman -Rh`
