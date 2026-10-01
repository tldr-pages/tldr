# fdisk

> Beheer partitietabellen en partities op een opslagschijf.
> Zie ook: `partprobe`, `parted`, `cfdisk`.
> Meer informatie: <https://manned.org/fdisk>.

- Toon partities:

`sudo fdisk {{[-l|--list]}}`

- Start de interactieve partitiemanipulator:

`sudo fdisk {{/dev/sdX}}`

- Open een hulp[m]enu:

`<m>`

- Toon de [p]artitietabel:

`<p>`

- Maak een [n]ieuwe partitie:

`<n>`

- Selecteer een partitie om te verwij[d]eren:

`<d>`

- Schrijf ([w]) gemaakte veranderingen:

`<w>`

- Verwijder gemaakte veranderingen en sluit ([q]) het programma af:

`<q>`
