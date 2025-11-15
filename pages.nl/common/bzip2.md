# bzip2

> Een blok-sorteer bestandscompressor.
> Zie ook: `bzcat`, `bunzip2`, `bzip2recover`.
> Meer informatie: <https://manned.org/bzip2>.

- Comprimeer een bestand:

`bzip2 {{pad/naar/bestand_te_comprimeren}}`

- Decomprimeer een bestand:

`bzip2 {{[-d|--decompress]}} {{pad/naar/gecomprimeerd_bestand.bz2}}`

- Decomprimeer een bestand naar `stdout`:

`bzip2 {{[-dc|--decompress --stdout]}} {{pad/naar/gecomprimeerd_bestand.bz2}}`

- Test de integriteit van elk bestand in het archiefbestand:

`bzip2 {{[-t|--test]}} {{pad/naar/gecomprimeerd_bestand.bz2}}`

- Toon de compressieverhouding voor elk verwerkt bestand met gedetailleerde informatie:

`bzip2 {{[-v|--verbose]}} {{pad/naar/gecomprimeerd_bestand.bz2}}`

- Decomprimeer een bestand en overschrijf bestaande bestanden:

`bzip2 {{[-f|--force]}} {{pad/naar/gecomprimeerd_bestanden.bz2}}`

- Toon de help:

`bzip2 {{[-h|--help]}}`
