# xz

> Comprimeren of decomprimeren van `.xz` en `.lzma` bestanden.
> Meer informatie: <https://manned.org/xz>.

- Comprimeer een bestand gebruik makend van xz file:

`xz {{pad/naar/bestand}}`

- Decomprimer een xz bestand:

`xz --decompress {{pad/naar/bestand.xz}}`

- Comprimeer een bestand gebruik makend van lzma:

`xz --format=lzma {{pad/naar/bestand}}`

- Decomprimer een lzma bestand:

`xz --decompress --format=lzma {{pad/naar/bestand.lzma}}`

- Decomprimer een bestand en schrijf het naar `stdout` (impliceert `--keep`):

`xz --decompress --stdout {{pad/naar/bestand.xz}}`

- Comprimeer een bestand, maar verwijder het origineel niet:

`xz --keep {{pad/naar/bestand}}`

- Comprimeer een bestand, gebruik makend van de snelste compressie:

`xz -0 {{pad/naar/bestand}}`

- Comprimeer een bestand, gebruik makend van de beste compressie:

`xz -9 {{pad/naar/bestand}}`
