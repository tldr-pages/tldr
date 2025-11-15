# pamditherbw

> Pas dithering toe op een grijze afbeelding, zet het bijvoorbeeld om in een patroon van een zwarte en witte pixels die eruitzien als de originele grijstinten.
> Zie ook: `pbmreduce`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

- Lees een PGM afbeelding, pas dithering toe en sla het op naar een bestand:

`pamditherbw {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Gebruik de gespecificeerde kwantificering methode:

`pamditherbw -{{floyd|fs|atkinson|threshold|hilbert|...}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Gebruik de atkinson kwantificering methode en de gespecifieerde seed voor een pseudo-random nummer generator:

`pamditherbw {{[-a|-atkinson]}} {{[-r|-randomseed]}} {{1337}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Specificeer de drempel waarde van de kwantificering methodes die een vorm van drempels uitvoeren:

`pamditherbw -{{fs|atkinson|thresholding}} {{[-va|-value]}} {{0.3}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`
