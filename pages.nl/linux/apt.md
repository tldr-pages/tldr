# apt

> Hulpprogramma voor pakketbeheer voor op Debian gebaseerde distributies.
> Aanbevolen vervanging voor `apt-get` bij interactief gebruik in Ubuntu versie 16.04 en later.
> Voor gelijkwaardige commando's in andere pakket managers, zie <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Meer informatie: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Werk de lijst van beschikbare pakketten en versies bij (het wordt aanbevolen dit uit te voeren voor elk ander `apt` commando):

`sudo apt update`

- Zoek naar een bepaald pakket:

`apt search {{package}}`

- Toon informatie over een pakket:

`apt show {{package}}`

- Installeer of werk het pakket bij naar de laatste beschikbare versie:

`sudo apt install {{package}}`

- Een pakket verwijderen (door in plaats daarvan `purge` te gebruiken, worden ook de configuratiebestanden verwijderd):

`sudo apt remove {{package}}`

- Upgrade alle geïnstalleerde pakketten naar hun nieuwste beschikbare versies:

`sudo apt upgrade`

- Maak een lijst van alle pakketten:

`apt list`

- Maak een lijst van alle geïnstalleerde pakketten:

`apt list --installed`
