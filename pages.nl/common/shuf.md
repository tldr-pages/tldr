# shuf

> Genereer willekeurige permutaties.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/shuf-invocation.html>.

- Wijzig willekeurig de volgorde van regels in een bestand en toon het resultaat:

`shuf {{pad/naar/bestand}}`

- Toon alleen de eerste 5 regels van het resultaat:

`shuf --head-count=5 {{pad/naar/bestand}}`

- Schrijf de uitvoer naar een ander bestand:

`shuf {{pad/naar/invoer_bestand}} --output={{pad/naar/uitvoer_bestand}}`

- Genereer 3 willekeurige getallen in het bereik van 1 tot 10 (inclusief):

`shuf --head-count=3 --input-range=1-10 --repeat`
