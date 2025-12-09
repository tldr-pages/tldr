# tail

> Toon het laatste deel van een bestand.
> Zie ook: `head`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Toon de laatste 10 regels van een bestand:

`tail {{pad/naar/bestand}}`

- Toon de laatste 10 regels van meerdere bestanden:

`tail {{path/to/file1 path/to/file2 ...}}`

- Toon laatste 5 regels in een bestand:

`tail {{[-5|--lines 5]}} {{pad/naar/bestand}}`

- Toon een bestand vanaf een specifiek regelnummer:

`tail {{[-n|--lines]}} +{{aantal}} {{pad/naar/bestand}}`

- Toon een specifiek aantal bytes vanaf het einde van een opgegeven bestand:

`tail {{[-c|--bytes]}} {{aantal}} {{pad/naar/bestand}}`

- Toon de laatste regels van een bestand en blijf het bestand lezen tot `<Ctrl c>`:

`tail {{[-f|--follow]}} {{pad/naar/bestand}}`

- Blijf het bestand lezen tot `<Ctrl c>`, ook als het bestand niet toegangelijk is:

`tail {{[-F|--retry --follow]}} {{pad/naar/bestand}}`

- Toon de laatste `aantal` regels in een bestand en ververs iedere `seconden` seconden:

`tail {{[-n|--lines]}} {{aantal}} {{[-s|--sleep-interval]}} {{seconden}} {{[-f|--follow]}} {{pad/naar/bestand}}`
