# xz

> Comprimeren of decomprimeren van XZ en LZMA bestanden.
> Meer informatie: <https://manned.org/xz>.

- Comprimeer een bestand gebruik makend van xz file:

`xz {{pad/naar/bestand}}`

- Decomprimer een xz bestand:

`xz {{[-d|--decompress]}} {{pad/naar/bestand.xz}}`

- Comprimeer een bestand gebruik makend van lzma:

`xz {{[-F|--format]}} lzma {{pad/naar/bestand}}`

- Decomprimer een LZMA bestand:

`xz {{[-d|--decompress]}} {{[-F|--format]}} lzma {{pad/naar/bestand.lzma}}`

- Decomprimer een bestand en schrijf het naar `stdout` (impliceert `--keep`):

`xz {{[-d|--decompress]}} {{[-c|--stdout]}} {{pad/naar/bestand.xz}}`

- Comprimeer een bestand, maar verwijder het origineel niet:

`xz {{[-k|--keep]}} {{pad/naar/bestand}}`

- Comprimeer een bestand, gebruik makend van de snelste compressie:

`xz -0 {{pad/naar/bestand}}`

- Comprimeer een bestand, gebruik makend van de beste compressie:

`xz -9 {{pad/naar/bestand}}`
