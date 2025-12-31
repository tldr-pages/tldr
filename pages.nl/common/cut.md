# cut

> Snij velden eruit vanuit `stdin` of bestanden.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>.

- Toon het vijfde teken van elke regel:

`{{commando}} | cut {{[-c|--characters]}} 5`

- Toon het vijfde tot en met tiende teken van elke regel van het opgegeven bestand:

`cut {{[-c|--characters]}} 5-10 {{pad/naar/bestand}}`

- Splits elke regel van een bestand op basis van een scheidingsteken in velden en toon velden twee en zes (standaard scheidingsteken is `TAB`):

`cut {{[-f|--fields]}} 2,6 {{pad/naar/bestand}}`

- Splits elke regel met het opgegeven scheidingsteken en toon alles vanaf het tweede veld:

`{{commando}} | cut {{[-d|--delimiter]}} "{{scheidingsteken}}" {{[-f|--fields]}} 2-`

- Gebruik een spatie als scheidingsteken en toon alleen de eerste drie velden:

`{{commando}} | cut {{[-d|--delimiter]}} " " {{[-f|--fields]}} -3`

- Toon specifieke velden van regels die `NUL` gebruiken om regels af te sluiten in plaats van newlines:

`{{find . -print0}} | cut {{[-z|--zero-terminated]}} {{[-d|--delimiter]}} "{{/}}" {{[-f|--fields]}} {{2}}`
