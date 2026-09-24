# pacman-mirrors

> Genereer een `pacman`-mirrorlist voor Manjaro Linux.
> Elke uitvoering van `pacman-mirrors` vereist dat je je database synchroniseert en je systeem bijwerkt met `sudo pacman -Syyu`.
> Zie ook: `pacman`.
> Meer informatie: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Genereer een mirrorlist met de standaardinstellingen:

`sudo pacman-mirrors --fasttrack`

- Verkrijg de status van de huidige mirrors:

`pacman-mirrors --status`

- Toon de huidige branch:

`pacman-mirrors --get-branch`

- Schakel over naar een andere branch:

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- Genereer een mirrorlist, waarbij alleen mirrors in jouw land worden gebruikt:

`sudo pacman-mirrors --geoip`
