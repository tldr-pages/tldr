# tail

> Toon het laatste deel van een bestand.
> Bekijk ook: `head`.
> Meer informatie: <https://keith.github.io/tail.1.html>.

- Toon laatste aantal regels in een bestand:

`tail -n {{8}} {{pad/naar/bestand}}`

- Toon een bestand vanaf een specifiek regelnummer:

`tail -n +{{8}} {{pad/naar/bestand}}`

- Toon een specifiek aantal bytes vanaf het einde van een opgegeven bestand:

`tail -c {{8}} {{pad/naar/bestand}}`

- Toon de laatste regels van een bestand en blijf het bestand lezen tot `Ctrl + C`:

`tail -f {{pad/naar/bestand}}`

- Blijf het bestand lezen tot `Ctrl + C`, ook als het bestand niet toegangelijk is:

`tail -F {{pad/naar/bestand}}`

- Toon de laatste aantal regels in een bestand en ververs iedere 'n' seconden:

`tail -n {{8}} -s {{10}} -f {{pad/naar/bestand}}`
