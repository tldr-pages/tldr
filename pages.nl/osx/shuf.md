# shuf

> Genereer willekeurige permutaties.
> Meer informatie: <https://manpagez.com/man/1/shuf/>.

- Wijzig willekeurig de volgorde van regels in een bestand en toon het resultaat:

`shuf {{pad/naar/bestand}}`

- Toon alleen de eerste 5 regels van het resultaat:

`shuf --head-count=5 {{pad/naar/bestand}}`

- Schrijf de uitvoer naar een ander bestand:

`shuf {{pad/naar/invoer_bestand}} --output {{pad/naar/uitvoer_bestand}}`

- Genereer willekeurige getallen in het bereik van 1 tot 10:

`shuf --input-range=1-10`
