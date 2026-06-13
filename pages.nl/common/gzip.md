# gzip

> Comprimeer/decomprimeer bestanden met `gzip`-compressie (LZ77).
> Meer informatie: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Comprimeer een bestand en vervang deze met een `gzip`-archief:

`gzip {{pad/naar/bestand}}`

- Decomprimeer een bestand en vervang deze met de originele, ongecomprimeerde versie:

`gzip {{[-d|--decompress]}} {{pad/naar/bestand.gz}}`

- Toon de naam en reductiepercentage voor elk gecomprimeerd bestand:

`gzip {{[-v|--verbose]}} {{pad/naar/bestand.gz}}`

- Comprimeer een bestand en behoud het originele bestand:

`gzip {{[-k|--keep]}} {{pad/naar/bestand}}`

- Comprimeer een bestand en geef de uitvoerbestandsnaam op:

`gzip {{[-c|--stdout]}} {{pad/naar/bestand}} > {{pad/naar/gecomprimeerd_bestand.gz}}`

- Decomprimeer een `gzip`-archief en geef de uitvoerbestandsnaam op:

`gzip {{[-cd|--stdout --decompress]}} {{pad/naar/bestand.gz}} > {{pad/naar/gedecomprimeerd_bestand}}`

- Specificeer het compressieniveau. 1 is het snelst (lage compressie), 9 is het traagst (hoge compressie) en 6 is de standaard:

`gzip -{{1..9}} {{[-c|--stdout]}} {{pad/naar/bestand}} > {{pad/naar/gecomprimeerd_bestand.gz}}`

- Toon de inhoud van een gecomprimeerd bestand:

`gzip {{[-l|--list]}} {{pad/naar/bestand.txt.gz}}`
