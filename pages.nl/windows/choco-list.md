# choco list

> Toon een lijst van pakketten met Chocolatey.
> Meer informatie: <https://chocolatey.org/docs/commands-list>.

- Toon alle beschikbare pakketten:

`choco list`

- Toon alle lokaal geïnstalleerde pakketten:

`choco list --local-only`

- Toon een lijst inclusief lokale programma's:

`choco list {{[-i|--include-programs]}}`

- Toon alleen goedgekeurde pakketten:

`choco list --approved-only`

- Geef een aangepaste bron op om pakketten van weer te geven:

`choco list {{[-s|--source]}} {{bron_url|alias}}`

- Geef een gebruikersnaam en wachtwoord voor authenticatie op:

`choco list --user {{gebruikersnaam}} --password {{wachtwoord}}`
