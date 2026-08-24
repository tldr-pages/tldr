# pacman --upgrade

> Arch Linux Paketverwaltungs-Werkzeug.
> Siehe auch: `pacman`.
> Weitere Informationen: <https://manned.org/pacman.8>.

- Installiere ein oder mehrere Pakete von Dateien:

`sudo pacman -U {{pfad/zu/paket1.pkg.tar.zst pfad/zu/paket2.pkg.tar.zst ...}}`

- Installiere ein Paket ohne Bestätigungsaufforderung:

`sudo pacman -U --noconfirm {{pfad/zu/paket.pkg.tar.zst}}`

- Überschreibe widersprüchliche Dateien während einer Paketinstallation:

`sudo pacman -U --overwrite {{pfad/zu/datei}} {{pfad/zu/paket.pkg.tar.zst}}`

- Installiere ein Paket und überspringe die Überprüfung von Abhängigkeitsversionen:

`sudo pacman -Ud {{pfad/zu/paket.pkg.tar.zst}}`

- Liste Pakete auf, welche betroffen sein würden (installiert keine Pakete):

`pacman -Up {{pfad/zu/paket.pkg.tar.zst}}`

- Zeige Hilfe an:

`pacman -Uh`
