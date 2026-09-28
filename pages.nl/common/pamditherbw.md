# pamditherbw

> Pas dithering toe op een grijze afbeelding, d.w.z. zet het om in een patroon van zwarte en witte pixels die eruitzien als de originele grijstinten.
> Zie ook: `pbmreduce`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

- Lees een PGM afbeelding, pas dithering toe en sla het op naar een bestand:

`pamditherbw {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Gebruik de gespecificeerde kwantisatiemethode:

`pamditherbw -{{floyd|fs|atkinson|threshold|hilbert|...}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Gebruik de atkinson kwantisatiemethode en de gespecificeerde seed voor een pseudo-random nummer generator:

`pamditherbw {{[-a|-atkinson]}} {{[-r|-randomseed]}} {{1337}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Specificeer de drempelwaarde van de kwantisatiemethodes die een vorm van drempels uitvoeren:

`pamditherbw -{{fs|atkinson|thresholding}} {{[-va|-value]}} {{0.3}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`
