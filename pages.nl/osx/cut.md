# cut

> Snij velden eruit vanuit `stdin` of bestanden.
> Meer informatie: <https://manned.org/man/freebsd-13.0/cut.1>.

- Toon een specifiek karakter/veldbereik voor iedere regel:

`{{commando}} | cut -{{c|f}} {{1|1,10|1-10|1-|-10}}`

- Toon een bereik voor iedere regel met een specifieke scheiding:

`{{commando}} | cut -d "{{,}}" -f {{1}}`

- Toon een bereik van iedere regel voor een specifiek bestand:

`cut -c {{1}} {{pad/naar/bestand}}`
