# pacman --files

> Arch Linux Paketverwaltungs-Werkzeug.
> Siehe auch `pkgfile`.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Zeige Hilfe an:

`pacman --files --help`

- Aktualisiere die Paketdatenbank:

`sudo pacman --files --refresh`

- Finde das Paket, welches eine bestimmte Datei besitzt:

`pacman --files {{dateiname}}`

- Finde das Paket, welches eine bestimmte Datei besitzt, mittels eines regulären Ausdrucks:

`pacman --files --regex '{{suchmuster}}'`

- Liste nur Paketnamen auf:

`pacman --files --quiet {{dateiname}}`

- Liste die Dateien auf welche einem bestimmten Paket gehören:

`pacman --files --list {{paketname}}`

- Liste nur den absoluten Pfad der Dateien auf:

`pacman --query --list --quiet {{paketname}}`
