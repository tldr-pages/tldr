# choco

> De Chocolatey pakket manager.
> Sommige subcommando's zoals `install`, `upgrade`, `pin` hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://docs.chocolatey.org/en-us/choco/commands/>.

- Installeer een pakket:

`choco install {{pakketnaam}}`

- Upgrade een specifiek geïnstalleerd pakket:

`choco upgrade {{pakketnaam}}`

- Upgrade alle verouderde pakketten en bevestig automatisch alle vragen:

`choco upgrade all {{[-y|--yes]}}`

- Verwijder een pakket en bevestig automatisch alle vragen:

`choco uninstall {{pakketnaam}} {{[-y|--yes]}}`

- Zoek voor pakketten op naam of sleutelwoord:

`choco search {{query}}`

- Toon alle geïnstalleerde pakketten:

`choco list`

- Toon pakketten die verouderd zijn:

`choco outdated`

- Installeer een pakket van een specifieke bron:

`choco install {{pakketnaam}} {{[-s|--source]}} {{bron}}`
