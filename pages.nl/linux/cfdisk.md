# cfdisk

> Beheer partitietabellen en partities op een harde schijf met het gebruik van een curses UI.
> Zie ook: `parted`.
> Meer informatie: <https://manned.org/cfdisk>.

- Start de partitiemanipulator met een specifiek apparaat:

`sudo cfdisk {{/dev/sdX}}`

- Creëer een nieuwe partitietabel voor een specifiek apparaat en beheer het:

`sudo cfdisk {{[-z|--zero]}} {{/dev/sdX}}`
