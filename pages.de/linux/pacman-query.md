# pacman --query

> Arch Linux Paketverwaltungs-Werkzeug.
> Siehe auch: `pacman`.
> Weitere Informationen: <https://manned.org/pacman.8>.

- Liste alle installierten Pakete und dessen Versionen auf:

`pacman -Q`

- Liste alle ausdrücklich installierten Pakete und dessen Versionen auf:

`pacman -Qe`

- Finde heraus welches Paket eine Datei besitzt:

`pacman -Qo {{dateiname}}`

- Zeige Informationen über ein installiertes Paket an:

`pacman -Qi {{paketname}}`

- Liste alle Dateien auf welche einem Paket gehören:

`pacman -Ql {{paketname}}`

- Liste verwaiste Pakete auf (Pakete welche als Abhängigkeit installiert wurden, aber von keinem Paket benötigt werden):

`pacman -Qdtq`

- Liste installierte Pakete auf welche nicht in den Repositorien gefunden werden können:

`pacman -Qm`

- Liste veraltete Pakete auf:

`pacman -Qu`
