# lrzip

> Een programma voor het comprimeren van grote bestanden.
> Zie ook: `lrunzip`, `lrztar`, `lrzuntar`.
> Meer informatie: <https://manned.org/lrzip>.

- Comprimeer een bestand met LZMA - langzame compressie, snelle decompressie:

`lrzip {{pad/naar/bestand}}`

- Comprimeer een bestand met BZIP2 - goede middenweg voor compressie/snelheid:

`lrzip {{[-b|--bzip2]}} {{pad/naar/bestand}}`

- Comprimeer met ZPAQ - extreme compressie, maar erg langzaam:

`lrzip {{[-z|--zpaq]}} {{pad/naar/bestand}}`

- Comprimeer met LZO - lichte compressie, extreem snelle decompressie:

`lrzip {{[-l|--lzo]}} {{pad/naar/bestand}}`

- Een bestand comprimeren en met een wachtwoord beveiligen/versleutelen:

`lrzip {{[-e|--encrypt]}} {{pad/naar/bestand}}`

- Overschrijf het aantal processor threads om te gebruiken:

`lrzip {{[-p|--threads]}} {{8}} {{pad/naar/bestand}}`
