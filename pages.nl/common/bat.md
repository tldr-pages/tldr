# bat

> Bestanden tonen en samenvoegen.
> Een `cat` kopie met syntax highlighting en Git integratie.
> Meer informatie: <https://github.com/sharkdp/bat>.

- Toon de inhoud van een of meerdere bestanden in `stdout`:

`bat {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Voeg verschillende bestanden samen in het doelbestand:

`bat {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/doelbestand}}`

- Verwijder decoraties en schakel paging uit (`--style plain` kan vervangen worden met `-p` of beide opties met `-pp`):

`bat --style plain --pager never {{pad/naar/bestand}}`

- Highlight een specifieke regel of een reeks van regels met een andere achtergrondkleur:

`bat {{--highlight-line|-H}} {{10|5:10|:10|10:|10:+5}} {{pad/naar/bestand}}`

- Toon niet-printbare karakters zoals spatie, tab of witregel:

`bat {{--show-all|-A}} {{pad/naar/bestand}}`

- Nummer alle uitvoerregels:

`bat {{--number|-n}} {{pad/naar/bestand}}`

- Highlight de syntax van een JSON-bestand:

`bat {{--language|-l}} json {{pad/naar/bestand.json}}`

- Toon alle ondersteunde talen:

`bat {{--list-languages|-L}}`
