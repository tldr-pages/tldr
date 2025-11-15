# dpkg

> Debian pakketbeheerder.
> Sommige subcommando's zoals `deb` hebben hun eigen gebruiksdocumentatie.
> Voor gelijkwaardige commando's in andere pakket managers, zie <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Meer informatie: <https://manned.org/dpkg>.

- Installeer een pakket:

`dpkg {{[-i|--install]}} {{pad/naar/bestand.deb}}`

- Verwijder een pakket:

`dpkg {{[-r|--remove]}} {{pakket}}`

- Toon geïnstalleerde pakketten:

`dpkg {{[-l|--list]}} {{patroon}}`

- Toon de inhoud van een pakket:

`dpkg {{[-L|--listfiles]}} {{pakket}}`

- Toon de inhoud van een lokaal pakketbestand:

`dpkg {{[-c|--contents]}} {{pad/naar/bestand.deb}}`

- Zoek uit welk pakket een bestand bezit:

`dpkg {{[-S|--search]}} {{pad/naar/bestand}}`

- Schoon een geïnstalleerd of al verwijderd pakket op, inclusief configuratie:

`dpkg {{[-P|--purge]}} {{pakket}}`
