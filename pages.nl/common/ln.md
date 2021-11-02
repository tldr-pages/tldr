# ln

> Maakt een verwijzing naar bestanden en mappen.
> Meer informatie: <https://www.gnu.org/software/coreutils/ln>.

- Maak een symbolische verwijzing naar een bestand of map:

`ln -s {{/pad/naar/bestand_of_map}} {{pad/naar/symbolische_verwijzing}}`

- Overschrijf een bestaande symbolische verwijzing om die naar een ander bestand te verwijzen:

`ln -sf {{/pad/naar/nieuw_bestand}} {{pad/naar/symbolische_verwijzing}}`

- Maak een harde verwijzing naar een bestand:

`ln {{/pad/naar/bestand}} {{pad/naar/harde_verwijzing}}`
