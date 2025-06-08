# lrztar

> Een wrapper voor `lrzip` om het comprimeren van mappen te vereenvoudigen.
> Zie ook: `tar`, `lrzuntar`, `lrunzip`.
> Meer informatie: <https://manned.org/lrztar>.

- Archiveer een map met tar en comprimeer dan:

`lrztar {{pad/naar/map}}`

- Hetzelfde als hierboven, met ZPAQ - extreme compressie, maar erg langzaam:

`lrztar -z {{pad/naar/map}}`

- Geef het uitvoerbestand op:

`lrztar -o {{pad/naar/bestand}} {{pad/naar/map}}`

- Overschrijf het aantal processor threads dat gebruikt moet worden:

`lrztar -p {{8}} {{pad/naar/map}}`

- Forceer het overschrijven van bestaande bestanden:

`lrztar -f {{pad/naar/map}}`
