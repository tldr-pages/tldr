# pamditherbw

> Pas dithering toe op een grijsschaalafbeelding, d.w.z. zet deze om in een patroon van zwarte en witte pixels die eruitzien als de originele grijsschaal.
> Zie ook: `pbmreduce`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

- Lees een PGM afbeelding, pas dithering toe en sla deze op in een bestand:

`pamditherbw {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Gebruik de gespecificeerde kwantisatiemethode:

`pamditherbw -{{floyd|fs|atkinson|threshold|hilbert|...}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Gebruik de atkinson kwantisatiemethode en de gespecificeerde seed voor een pseudo-random getallengenerator:

`pamditherbw {{[-a|-atkinson]}} {{[-r|-randomseed]}} {{1337}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`

- Specificeer de drempelwaarde van de kwantisatiemethodes die een vorm van drempels uitvoeren:

`pamditherbw -{{fs|atkinson|thresholding}} {{[-va|-value]}} {{0.3}} {{pad/naar/afbeelding.pgm}} > {{pad/naar/bestand.pgm}}`
