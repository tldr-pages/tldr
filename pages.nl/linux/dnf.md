# dnf

> Hulpprogramma voor pakketbeheer van RHEL, Fedora en CentOS (vervangt Yum).
> Voor gelijkwaardige commando's binnen andere pakketbeheer, zie <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Meer informatie: <https://dnf.readthedocs.io>.

- Upgrade geïnstalleerde pakketten naar de nieuwste beschikbare versies:

`sudo dnf {{[up|upgrade]}}`

- Zoek naar pakketten via sleutelwoorden:

`dnf {{[se|search]}} {{sleutelwoord1 sleutelwoord2 ...}}`

- Toon gedetailleerde informatie over een pakket:

`dnf {{[if|info]}} {{pakket}}`

- Installeer nieuwe pakketten (gebruik `--assumeyes` om alle prompts automatisch te bevestigen):

`sudo dnf {{[in|install]}} {{pakket1 pakket2 ...}}`

- Verwijder een pakket:

`sudo dnf {{[rm|remove]}} {{pakket1 pakket2 ...}}`

- Toon alle geïnstalleerde pakketten:

`dnf {{[ls|list]}} --installed`

- Vind welk pakket voorziet van een bepaald commando:

`dnf {{[wp|provides]}} {{commando}}`

- Toon alle historische operaties:

`dnf {{[hist|history]}}`
