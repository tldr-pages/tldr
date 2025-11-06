# Clear-History

> Verwijder vermeldingen uit de Powershell-sessie commandogeschiedenis.
> Opmerking: `clhy` kan gebruikt worden als een alias voor `Clear-History`.
> Meer informatie: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/clear-history>.

- Verwijder alle geschiedenis van de huidige sessie:

`Clear-History`

- Verwijder commando op exacte naam:

`Clear-History -CommandLine "{{commando}}"`

- Verwijder meerdere commando's op naam:

`Clear-History -CommandLine {{"commando1", "commando2", ...}}`

- Verwijder een specifiek geschiedenisvermelding op ID:

`Clear-History -Id {{id_nummer}}`

- Verwijder meerdere ID's:

`Clear-History -Id {{id1, id2, ...}}`

- Verwijder opdrachten binnen een bereik van ID's:

`Clear-History -Id ({{start_id}}..{{eind_id}})`

- Toon wat er verwijderd zou worden:

`Clear-History -WhatIf`

- Vraag om bevestiging voor het verwijderen:

`Clear-History -Confirm`
