# bun create

> Maak een nieuw project van een sjabloon.
> Opmerking: `c` kan gebruikt worden als alias voor `create`.
> Meer informatie: <https://bun.com/docs/runtime/templating/create>.

- Maak interactief een nieuw project van een officieel sjabloon:

`bun create {{template}}`

- Maak een nieuw project van een officiële sjabloon in een nieuwe map:

`bun create {{template}} {{pad/naar/bestemming}}`

- Maak een nieuw project van een GitHub repository sjabloon:

`bun create {{https://github.com/gebruikersnaam/repo}} {{pad/naar/bestemming}}`

- Maak een nieuw project van een lokaal sjabloon:

`bun create {{path/to/template}} {{pad/naar/bestemming}}`

- Maak een nieuw project en overschrijf de doelmap als deze bestaat:

`bun create {{template}} {{pad/naar/bestemming}} --force`

- Maak een nieuw project zonder automatisch een Git repository te initialiseren:

`bun create {{template}} {{pad/naar/bestemming}} --no-git`

- Maak een nieuw project zonder automatisch afhankelijkheden te installeren:

`bun create {{template}} {{pad/naar/bestemming}} --no-install`
