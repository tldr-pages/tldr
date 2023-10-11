# paru

> Ein AUR-Helfer und pacman-Wrapper.
> Weitere Informationen: <https://github.com/Morganamilo/paru>.

- Interaktiv nach einem Paket suchen und es installieren:

`paru {{paketname_oder_suchbegriff}}`

- Alle Pakete synchronisieren und aktualisieren:

`paru`

- AUR-Pakete aktualisieren:

`paru -Sua`

- Informationen über ein Paket abrufen:

`paru -Si {{paketname}}`

- Herunterladen von `PKGBUILD` und anderen Paket-Quelldateien aus dem AUR oder dem ABS:

`paru --getpkgbuild {{paketname}}`

- Anzeigen der `PKGBUILD`-Datei eines Pakets:

`paru --getpkgbuild --print {{paketname}}`
