# pamditherbw

> Pas dithering toe op een grijze afbeelding, zet het bijvoorbeeld om in een patroon van een zwarte en witte pixels die eruitzien als de originele grijstinten.
> Bekijk ook: `pbmreduce`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

- Lees een PGM afbeelding, pas dithering toe en sla het op naar een bestand:

`ppmditherbw {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Gebruik de gespecificeerde kwantificering methode:

`ppmditherbw -{{floyd|fs|atkinson|threshold|hilbert|...}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Gebruik de atkinson kwantificering methode en de gespecifieerde seed voor een pseudo-random nummer generator:

`ppmditherbw -atkinson -randomseed {{1337}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Specificeer de drempel waarde van de kwantificering methodes die een vorm van drempels uitvoeren:

`ppmditherbw -{{fs|atkinson|thresholding}} -value {{0.3}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`
