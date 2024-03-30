# tail

> Toon het laatste deel van een bestand.
> Bekijk ook: `head`.
> Meer informatie: <https://www.gnu.org/software/coreutils/tail>.

- Toon laatste aantal regels in een bestand:

`tail --lines {{aantal}} {{pad/naar/bestand}}`

- Toon een bestand vanaf een specifiek regelnummer:

`tail --lines +{{aantal}} {{pad/naar/bestand}}`

- Toon een specifiek aantal bytes vanaf het einde van een opgegeven bestand:

`tail --bytes {{aantal}} {{pad/naar/bestand}}`

- Toon de laatste regels van een bestand en blijf het bestand lezen tot `Ctrl + C`:

`tail --follow {{pad/naar/bestand}}`

- Blijf het bestand lezen tot `Ctrl + C`, ook als het bestand niet toegangelijk is:

`tail --retry --follow {{pad/naar/bestand}}`

- Toon de laatste aantal regels in een bestand en ververs iedere 'n' seconden:

`tail --lines {{aantal}} --sleep-interval {{seconden}} --follow {{pad/naar/bestand}}`
