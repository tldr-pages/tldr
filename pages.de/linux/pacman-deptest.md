# pacman --deptest

> Überprüfe alle angegebenen Abhängigkeiten und gib eine Liste von Abhängigkeiten zurück, welche auf dem System nicht erfüllt sind.
> Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Zeige Paketnamen von Abhängigkeiten an, welche nicht installiert sind:

`pacman --deptest {{paketname1}} {{paketname2}}`

- Überprüfe ob ein installiertes Paket eine Minimalversion erfüllt:

`pacman --deptest "{{bash>=5}}"`

- Überprüfe ob eine neuere version eines Paketes installiert ist:

`pacman --deptest "{{bash>5}}"`

- Zeige Hilfe an:

`pacman --deptest --help`
