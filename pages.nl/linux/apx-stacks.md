# apx stacks

> Beheer stacks in `apx`.
> Let op: door gebruikers gecreëerde pakketbeheerconfiguraties worden opgeslagen in `~/.local/share/apx/pkgmanagers`.
> Meer informatie: <https://docs.vanillaos.org/docs/en/apx-manpage#stacks>.

- Maak interactief een nieuwe stack configuratie:

`apx stacks new`

- Update interactief een nieuwe stack configuratie:

`apx stacks update {{naam}}`

- Toon alle beschikbare stack configuraties:

`apx stacks list`

- Verwijder een specifieke stack configuratie:

`apx stacks rm --name {{string}}`

- Importeer een stack configuratie:

`apx stacks import --input {{pad/naar/stack.yml}}`

- Exporteer de stack configuratie (Let op: de output flag is optioneel, het wordt standaard geëxporteerd naar de huidige map):

`apx stacks export --name {{string}} --output {{pad/naar/output_bestand}}`
