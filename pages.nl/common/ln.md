# ln

> Maakt een verwijzing naar bestanden en mappen.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html>.

- Maak een symbolische verwijzing naar een bestand of map:

`ln {{[-s|--symbolic]}} /{{pad/naar/bestand_of_map}} {{pad/naar/symbolische_verwijzing}}`

- Maak een symbolische verwijziging relatief naar waar de link bestaat:

`ln {{[-s|--symbolic]}} {{pad/naar/bestand_of_map}} {{pad/naar/symbolische_verwijzing}}`

- Overschrijf een bestaande symbolische verwijzing om die naar een ander bestand te verwijzen:

`ln {{[-sf|--symbolic --force]}} /{{pad/naar/nieuw_bestand}} {{pad/naar/symbolische_verwijzing}}`

- Maak een harde verwijzing naar een bestand:

`ln /{{pad/naar/bestand}} {{pad/naar/harde_verwijzing}}`
