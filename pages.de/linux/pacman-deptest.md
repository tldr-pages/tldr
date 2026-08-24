# pacman --deptest

> Überprüfe alle angegebenen Abhängigkeiten und gib eine Liste von Abhängigkeiten zurück, welche auf dem System nicht erfüllt sind.
> Siehe auch: `pacman`.
> Weitere Informationen: <https://manned.org/pacman.8>.

- Zeige Paketnamen von Abhängigkeiten an, welche nicht installiert sind:

`pacman -T {{paket1 paket2 ...}}`

- Überprüfe ob ein installiertes Paket eine Minimalversion erfüllt:

`pacman -T "{{bash>=5}}"`

- Überprüfe ob eine neuere version eines Paketes installiert ist:

`pacman -T "{{bash>5}}"`

- Zeige Hilfe an:

`pacman -Th`
