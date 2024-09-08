# seq

> Toon een reeks getallen naar `stdout`.
> Meer informatie: <https://www.gnu.org/software/coreutils/seq>.

- Reeks van 1 tot 10:

`seq 10`

- Elk 3e nummer van 5 tot 20:

`seq 5 3 20`

- Scheid de uitvoer met een spatie in plaats van een nieuwe regel:

`seq -s " " 5 3 20`

- Formatteer de uitvoerbreedte naar minimaal 4 cijfers, opgevuld met nullen indien nodig:

`seq -f "%04g" 5 3 20`
