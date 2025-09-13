# lrzip

> Een programma voor het comprimeren van grote bestanden.
> Zie ook: `lrunzip`, `lrztar`, `lrzuntar`.
> Meer informatie: <https://manned.org/lrzip>.

- Comprimeer een bestand met LZMA - langzame compressie, snelle decompressie:

`lrzip {{pad/naar/bestand}}`

- Comprimeer een bestand met BZIP2 - goede middenweg voor compressie/snelheid:

`lrzip -b {{pad/naar/bestand}}`

- Comprimeer met ZPAQ - extreme compressie, maar erg langzaam:

`lrzip -z {{pad/naar/bestand}}`

- Comprimeer met LZO - lichte compressie, extreem snelle decompressie:

`lrzip -l {{pad/naar/bestand}}`

- Een bestand comprimeren en met een wachtwoord beveiligen/versleutelen:

`lrzip -e {{pad/naar/bestand}}`

- Overschrijf het aantal processor threads om te gebruiken:

`lrzip -p {{8}} {{pad/naar/bestand}}`
