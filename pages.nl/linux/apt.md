# apt

> Pakketbeheerder voor op Debian gebaseerde distributies.
> Gebruiksvriendelijk alternatief voor `apt-get` voor interactief gebruik.
> Voor gelijkwaardige commando's in andere pakket managers, zie <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Meer informatie: <https://manned.org/apt.8>.

- Werk de lijst van beschikbare pakketten en versies bij (het wordt aanbevolen dit uit te voeren voor elk ander `apt` commando):

`sudo apt update`

- Zoek naar pakketten op naam of beschrijving:

`apt search {{pakket}}`

- Zoek naar pakketten op naam (ondersteund wildcards zoals `*`):

`apt list {{pakket}}`

- Toon gedetailleerde informatie voor een specifiek pakket:

`apt show {{pakket}}`

- Installeer specifieke pakketten of werk ze bij naar de nieuwste versies:

`sudo apt install {{pakket}}`

- Verwijder specifieke pakketten (gebruik in plaats daarvan `purge` om ook hun configuratiebestanden te verwijderen):

`sudo apt remove {{pakket}}`

- Upgrade alle geïnstalleerde pakketten naar hun nieuwste versies:

`sudo apt upgrade`

- Toon alle geïnstalleerde pakketten:

`apt list {{[-i|--installed]}}`
