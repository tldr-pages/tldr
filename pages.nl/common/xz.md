# xz

> Comprimeren of decomprimeren van XZ en LZMA bestanden.
> Meer informatie: <https://manned.org/xz>.

- Comprimeer een bestand naar het XZ-formaat:

`xz {{pad/naar/bestand}}`

- Decomprimeer een XZ-bestand:

`xz {{[-d|--decompress]}} {{pad/naar/bestand.xz}}`

- Comprimeer een bestand gebruikmakend van LZMA:

`xz {{[-F|--format]}} lzma {{pad/naar/bestand}}`

- Decomprimeer een LZMA-bestand:

`xz {{[-d|--decompress]}} {{[-F|--format]}} lzma {{pad/naar/bestand.lzma}}`

- Decomprimeer een bestand en schrijf het naar `stdout` (impliceert `--keep`):

`xz {{[-d|--decompress]}} {{[-c|--stdout]}} {{pad/naar/bestand.xz}}`

- Comprimeer een bestand, maar verwijder het origineel niet:

`xz {{[-k|--keep]}} {{pad/naar/bestand}}`

- Comprimeer een bestand, gebruikmakend van de snelste compressie:

`xz -0 {{pad/naar/bestand}}`

- Comprimeer een bestand, gebruikmakend van de beste compressie:

`xz -9 {{pad/naar/bestand}}`
