# pacman --query

> Arch Linux pakketbeheer hulpprogramma.
> Zie ook: `pacman`.
> Meer informatie: <https://manned.org/pacman.8>.

- [Q]uery de lokale pakkettendatabase en toon geïnstalleerde pakketten en versies:

`pacman -Q`

- Toon alleen pakketten en versies welke [e]xpliciet geïnstalleerd zijn:

`pacman -Qe`

- Zoek welk pakket een bestand bezit ([o]):

`pacman -Qo {{bestandsnaam}}`

- Toon informatie over een geïnstalleerd ([i]) pakket:

`pacman -Qi {{pakket}}`

- Toon de [l]ijst met bestanden welke een specifiek pakket bezit:

`pacman -Ql {{pakket}}`

- Maak een lijst van pakketten welke geïnstalleerd zijn als afhankelijkhe[d]en maar niet vereist door een pakket en print in stille ([q]) modus (alleen pakketnaam wordt weergegeven):

`pacman -Qdtq`

- Toon geïnstalleerde pakketten foreign ([m]) voor de repository database:

`pacman -Qm`

- Toon pakketten die geüpgraded ([u]) kunnen worden:

`pacman -Qu`
