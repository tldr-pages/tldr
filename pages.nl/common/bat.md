# bat

> Bestanden tonen en samenvoegen.
> Een `cat` kopie met syntax highlighting en Git integratie.
> Meer informatie: <https://github.com/sharkdp/bat>.

- Toon de inhoud van een of meerdere bestanden in `stdout`:

`bat {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Voeg verschillende bestanden samen in het doelbestand:

`bat {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{doelbestand}}`

- Voeg verschillende bestanden toe aan het doelbestand:

`bat {{pad/naar/bestand1 pad/naar/bestand2 ...}} >> {{doelbestand}}`

- Nummer alle uitvoerregels:

`bat --number {{pad/naar/bestand}}`

- Highlight de syntax van een JSON-bestand:

`bat --language json {{pad/naar/bestand.json}}`

- Toon alle ondersteunde talen:

`bat --list-languages`
