# as

> Draagbare GNU assembler.
> Voornamelijk bedoeld om uitvoer van `gcc` te assembleren voor gebruik door `ld`.
> Meer informatie: <https://keith.github.io/xcode-man-pages/as.1.html>.

- Assembleer een bestand en schrijf de output naar `a.out`:

`as {{pad/naar/bestand.s}}`

- Assembleer de output naar een specifiek bestand:

`as {{pad/naar/bestand.s}} -o {{pad/naar/uitvoer_bestand.o}}`

- Genereer sneller output door spaties en commentaarvoorverwerking over te slaan. (Moet alleen worden gebruikt voor vertrouwde compilers):

`as -f {{pad/naar/bestand.s}}`

- Voeg een specifiek pad toe aan de lijst met mappen om te zoeken naar bestanden die zijn opgegeven in `.include`-richtlijnen:

`as -I {{pad/naar/directory}} {{pad/naar/bestand.s}}`
