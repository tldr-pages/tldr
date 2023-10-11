# dnf

> Hulpprogramma voor pakketbeheer van RHEL, Fedora en CentOS (vervangt Yum).
> Voor gelijkwaardige commando's binnen andere pakketbeheerders, zie <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Meer informatie: <https://dnf.readthedocs.io>.

- Upgrade geïnstalleerde pakketten naar de nieuwste beschikbare versies:

`sudo dnf upgrade`

- Zoek naar pakketten via sleutelwoorden:

`dnf search {{sleutelwoord1 sleutelwoord2 ...}}`

- Toon gedetailleerde informatie over een pakket:

`dnf info {{pakket}}`

- Installeer nieuwe pakketten (gebruik `-y` om alle prompts automatisch te bevestigen):

`sudo dnf install {{pakket1 pakket2 ...}}`

- Verwijder een pakket:

`sudo dnf remove {{pakket1 pakket2 ...}}`

- Toon alle geïnstalleerde pakketten:

`dnf list --installed`

- Vind welk pakket voorziet van een bepaald commando:

`dnf provides {{commando}}`

- Toon alle historische operaties:

`dnf history`
