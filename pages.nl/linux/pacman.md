# pacman

> Hulpprogramma voor het beheren van pakketten op Arch Linux.
> Zie ook: `pacman-sync`, `pacman-remove`, `pacman-query`, `pacman-upgrade`, `pacman-files`, `pacman-database`, `pacman-deptest`, `pacman-key`, `pacman-mirrors`.
> Voor gelijkwaardige commando's in andere pakket managers, zie <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Meer informatie: <https://manned.org/pacman.8>.

- [S]ynchroniseer en update alle pakketten:

`sudo pacman -Syu`

- Installeer een nieuw pakket:

`sudo pacman -S {{pakket}}`

- Verwijde[R] een pakket en zijn afhankelijkheden:

`sudo pacman -Rs {{pakket}}`

- Doorzoek ([s]) de pakketdatabase met een reguliere expressie of zoekwoord:

`pacman -Ss "{{zoekterm}}"`

- Zoek in de database voor pakketten die een specifiek bestand ([F]) bevatten:

`pacman -F "{{bestandsnaam}}"`

- Toon alleen de [e]xpliciet geïnstalleerde pakketten en versies:

`pacman -Qe`

- Toon weespakketten (geïnstalleerd als afhankelijkhe[d]en maar niet daadwerkelijk vereist door een ander pakket):

`pacman -Qtdq`

- Leeg de hele `pacman` cache:

`sudo pacman -Scc`
