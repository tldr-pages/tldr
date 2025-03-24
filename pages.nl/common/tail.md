# tail

> Toon het laatste deel van een bestand.
> Bekijk ook: `head`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Toon laatste aantal regels in een bestand:

`tail {{[-n|--lines]}} {{aantal}} {{pad/naar/bestand}}`

- Toon een bestand vanaf een specifiek regelnummer:

`tail {{[-n|--lines]}} +{{aantal}} {{pad/naar/bestand}}`

- Toon een specifiek aantal bytes vanaf het einde van een opgegeven bestand:

`tail {{[-n|--lines]}} {{aantal}} {{pad/naar/bestand}}`

- Toon de laatste regels van een bestand en blijf het bestand lezen tot `<Ctrl c>`:

`tail {{[-f|--follow]}} {{pad/naar/bestand}}`

- Blijf het bestand lezen tot `<Ctrl c>`, ook als het bestand niet toegangelijk is:

`tail {{[-F|--retry --follow]}} {{pad/naar/bestand}}`

- Toon de laatste aantal regels in een bestand en ververs iedere 'n' seconden:

`tail {{[-n|--lines]}} {{aantal}} {{[-s|--sleep-interval]}} {{seconden}} {{[-f|--follow]}} {{pad/naar/bestand}}`
