# apt

> Hulpprogramma voor pakketbeheer voor op Debian gebaseerde distributies.
> Aanbevolen vervanging voor `apt-get` bij interactief gebruik in Ubuntu versie 16.04 en later.
> Voor gelijkwaardige commando's in andere pakket managers, zie <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Meer informatie: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Werk de lijst van beschikbare pakketten en versies bij (het wordt aanbevolen dit uit te voeren voor elk ander `apt` commando):

`sudo apt update`

- Zoek naar een specifiek pakket:

`apt search {{pakket}}`

- Toon informatie voor een specifiek pakket:

`apt show {{pakket1 pakket2 ...}}`

- Installeer specifieke pakketten of werk ze bij naar de nieuwste beschikbare versies:

`sudo apt install {{pakket1 pakket2 ...}}`

- Verwijder specifieke pakketten (gebruik in plaats daarvan purge om ook hun configuratiebestanden te verwijderen):

`sudo apt remove {{pakket1 pakket2 ...}}`

- Upgrade alle geïnstalleerde pakketten naar hun nieuwste beschikbare versies:

`sudo apt upgrade`

- Maak een lijst van alle pakketten:

`apt list`

- Maak een lijst van alle geïnstalleerde pakketten:

`apt list --installed`
