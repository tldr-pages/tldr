# pamfix

> Repareer errors in PAM, PBM, PGM en PPM bestanden.
> Bekijk ook: `pamfile`, `pamvalidate`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamfix.html>.

- Repareer een Netpbm bestand dat zijn laatste deel mist:

`pamfix -truncate {{pad/naar/corrupt.ext}} > {{pad/naar/uitvoer.ext}}`

- Repareer een Netpbm bestand waar de pixel waardes de afbeelding's `maxval` overschrijden door de overtredende pixels te verlagen in waarde:

`pamfix -clip {{pad/naar/corrupt.ext}} > {{pad/naar/uitvoer.ext}}`

- Repareer een Netpbm bestand waar de pixel waardes de afbeelding's `maxval` overschrijden door deze te verhogen:

`pamfix -changemaxval {{pad/naar/corrupt.pam|pbm|pgm|ppm}} > {{pad/naar/uitvoer.pam|pbm|pgm|ppm}}`
