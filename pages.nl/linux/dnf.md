# dnf

> Pakketbeheerder voor Fedora 41+ en RHEL 10.
> Voor equivalente commando's in andere pakketbeheerders, zie <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Meer informatie: <https://dnf5.readthedocs.io/en/latest/commands/index.html>.

- Upgrade geïnstalleerde pakketten naar de nieuwste beschikbare versies:

`sudo dnf {{[up|upgrade]}}`

- Zoek naar pakketten via sleutelwoorden:

`dnf {{[se|search]}} {{sleutelwoord1 sleutelwoord2 ...}}`

- Toon gedetailleerde informatie over een pakket:

`dnf {{[if|info]}} {{pakket}}`

- Installeer nieuwe pakketten (gebruik `--assumeyes` om alle prompts automatisch te bevestigen):

`sudo dnf {{[in|install]}} {{pakket1 pakket2 ...}}`

- Verwijder pakketten:

`sudo dnf {{[rm|remove]}} {{pakket1 pakket2 ...}}`

- Toon alle geïnstalleerde pakketten:

`dnf {{[ls|list]}} --installed`

- Vind welke pakketten voorzien in een bepaald commando:

`dnf provides {{commando}}`

- Verwijder gecachte data:

`sudo dnf clean {{all|dbcache|expire-cache|metadata|packages}}`
