# pacman --files

> Arch Linux Paketverwaltungs-Werkzeug.
> Siehe auch: `pacman`, `pkgfile`.
> Weitere Informationen: <https://manned.org/pacman.8>.

- Aktualisiere die Paketdatenbank:

`sudo pacman -Fy`

- Finde das Paket, welches eine bestimmte Datei besitzt:

`pacman -F {{dateiname}}`

- Finde das Paket, welches eine bestimmte Datei besitzt, mittels eines regulären Ausdrucks:

`pacman -Fx '{{suchmuster}}'`

- Liste nur Paketnamen auf:

`pacman -Fq {{dateiname}}`

- Liste die Dateien auf welche einem bestimmten Paket gehören:

`pacman -Fl {{paketname}}`

- Zeige Hilfe an:

`pacman -Fh`
