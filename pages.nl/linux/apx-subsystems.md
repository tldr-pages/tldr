# apx subsystems

> Beheer subsystemen in `apx`.
> Subsystemen zijn containers die kunnen worden gemaakt op basis van reeds bestaande stapels.
> Meer informatie: <https://github.com/Vanilla-OS/apx>.

- Maak interactief een nieuw subsysteem:

`apx subsystems new`

- Toon alle beschikbare subsystemen:

`apx subsystems list`

- Reset een specifiek subsysteem naar zijn initiële toestand:

`apx subsystems reset --name {{string}}`

- [f]orceer een reset van een specifiek subsysteem:

`apx subsystems reset --name {{string}} --force`

- Verwijder een specifiek subsysteem:

`apx subsystems rm --name {{string}}`

- [f]orceer het verwijderen van een specifiek subsysteem:

`apx subsystems rm --name {{string}} --force`
