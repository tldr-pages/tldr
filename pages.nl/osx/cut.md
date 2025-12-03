# cut

> Snij velden eruit vanuit `stdin` of bestanden.
> Meer informatie: <https://keith.github.io/xcode-man-pages/cut.1.html>.

- Toon het vijfde teken ([c]) van elke regel:

`{{commando}} | cut -c 5`

- Toon het vijfde tot en met tiende teken ([c]) van elke regel van het opgegeven bestand:

`cut -c 5-10 {{pad/naar/bestand}}`

- Splits elke regel van een bestand op basis van een scheidingsteken in velden ([f]) en toon velden twee en zes (standaard scheidingsteken is `TAB`):

`cut -f 2,6 {{pad/naar/bestand}}`

- Splits elke regel met het opgegeven scheidingsteken ([d]) en toon alles vanaf het tweede veld:

`{{commando}} | cut -d "{{scheidingsteken}}" -f 2-`

- Gebruik een spatie als scheidingsteken ([d]) en toon alleen de eerste drie velden ([f]):

`{{commando}} | cut -d " " -f -3`
