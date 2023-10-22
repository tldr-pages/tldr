# pacman --upgrade

> Arch Linux Paketverwaltungs-Werkzeug.
> Siehe auch: `pacman`.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Installiere ein oder mehrere Pakete von Dateien:

`sudo pacman --upgrade {{pfad/zu/paket1.pkg.tar.zst}} {{pfad/zu/paket2.pkg.tar.zst}}`

- Installiere ein Paket ohne Bestätigungsaufforderung:

`sudo pacman --upgrade --noconfirm {{pfad/zu/paket.pkg.tar.zst}}`

- Überschreibe widersprüchliche Dateien während einer Paketinstallation:

`sudo pacman --upgrade --overwrite {{pfad/zu/datei}} {{pfad/zu/paket.pkg.tar.zst}}`

- Installiere ein Paket und überspringe die Überprüfung von Abhängigkeitsversionen:

`sudo pacman --upgrade --nodeps {{pfad/zu/paket.pkg.tar.zst}}`

- Liste Pakete auf, welche betroffen sein würden (installiert keine Pakete):

`pacman --upgrade --print {{pfad/zu/paket.pkg.tar.zst}}`

- Zeige Hilfe an:

`pacman --upgrade --help`
