# pacman --sync

> Arch Linux Paket Management tool.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8.de>.

- Installiere ein neues Paket:

`sudo pacman --sync {{paketname}}`

- Synchronisiere und aktualisiere alle Pakete (füge `--downloadonly` hinzu um die Pakete nur herunterzuladen und nicht zu aktualisieren):

`sudo pacman --sync --refresh --sysupgrade`

- Aktualisiere alle Pakete und installiere ein neues ohne eine Bestätigung aufzufordern:

`sudo pacman --sync --refresh --sysupgrade --noconfirm {{paketname}}`

- Suche in der Paketdatenbank mit einem regulärem Ausdruck oder Schlüsselwort:

`pacman --sync --search "{{suchmuster}}"`

- Zeige Informationen über ein Paket an:

`pacman --sync --info {{paketname}}`

- Überschreibe widersprüchliche Dateien während einer Paketaktualisierung:

`sudo pacman --sync --refresh --sysupgrade --overwrite {{pfad/zur/datei}}`

- Synchronisiere und aktualisiere alle Pakete, ignoriere aber ein spezifisches Paket (kann mehr als einmal genutzt werden):

`sudo pacman --sync --refresh --sysupgrade --ignore {{paketname}}`

- Entferne nicht installierte Pakete und ungenutzte Repositorien vom Cache (nutze zwei `--clean` Operationen um alle Pakete aufzuräumen):

`sudo pacman --sync --clean`
