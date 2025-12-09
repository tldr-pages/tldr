# seq

> Toon een reeks getallen naar `stdout`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html>.

- Toon een reeks van 1 tot 10:

`seq 10`

- Toon een reeks van 10 tot 20:

`seq 10 20`

- Toon ieder 3e nummer in een reeks van 5 tot 20:

`seq 5 3 20`

- Scheid de uitvoer met een spatie in plaats van een nieuwe regel:

`seq {{[-s|--separator]}} " " {{5 3 20}}`

- Formatteer de uitvoerbreedte naar minimaal 4 cijfers, opgevuld met nullen indien nodig:

`seq {{[-f|--format]}} "%04g" {{5 3 20}}`

- Toon alle nummers met dezelfde breedte:

`seq {{[-w|--equal-width]}} {{5 3 20}}`
