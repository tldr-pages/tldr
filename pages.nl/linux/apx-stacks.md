# apx stacks

> Beheer stapels in `apx`.
> Opmerking: door gebruikers gecreëerde stapelconfiguraties worden opgeslagen in `~/.local/share/apx/stacks`.
> Meer informatie: <https://docs.vanillaos.org/docs/en/apx-manpage#stacks>.

- Maak interactief een nieuwe stapelconfiguratie:

`apx stacks new`

- Update interactief een stapelconfiguratie:

`apx stacks update {{naam}}`

- Toon alle beschikbare stapelconfiguraties:

`apx stacks list`

- Verwijder een specifieke stapelconfiguratie:

`apx stacks rm --name {{string}}`

- Importeer een stapelconfiguratie:

`apx stacks import --input {{pad/naar/stack.yml}}`

- Exporteer de stapelconfiguratie (Let op: de output flag is optioneel, het wordt standaard geëxporteerd naar de huidige map):

`apx stacks export --name {{string}} --output {{pad/naar/output_bestand}}`
