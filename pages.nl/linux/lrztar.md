# lrztar

> Een wrapper voor `lrzip` om het comprimeren van mappen te vereenvoudigen.
> Zie ook: `tar`, `lrzuntar`, `lrunzip`.
> Meer informatie: <https://manned.org/lrztar>.

- Archiveer een map met tar en comprimeer dan:

`lrztar {{pad/naar/map}}`

- Hetzelfde als hierboven, met ZPAQ - extreme compressie, maar erg langzaam:

`lrztar {{[-z|--zpaq]}} {{pad/naar/map}}`

- Geef het uitvoerbestand op:

`lrztar {{[-o|--outfile]}} {{pad/naar/bestand}} {{pad/naar/map}}`

- Overschrijf het aantal processor threads dat gebruikt moet worden:

`lrztar {{[-p|--threads]}} {{8}} {{pad/naar/map}}`

- Forceer het overschrijven van bestaande bestanden:

`lrztar {{[-f|--force]}} {{pad/naar/map}}`
