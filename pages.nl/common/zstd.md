# zstd

> Bestanden comprimeren of decomprimeren met Zstandard compressie.
> Meer informatie: <https://github.com/facebook/zstd>.

- Comprimeer een bestand naar een nieuw bestand met de `.zst` extensie:

`zstd {{pad/naar/bestand}}`

- Decomprimeer een bestand:

`zstd --decompress {{pad/naar/bestand.zst}}`

- Decomprimeer naar `stdout`:

`zstd --decompress --stdout {{pad/naar/bestand.zst}}`

- Comprimeer een bestand met een specifiek compressie level, waar 1=snelste, 19=langzaamste en 3=standaard:

`zstd -{{level}} {{pad/naar/bestand}}`

- Ontgrendel hogere compressieniveaus (tot en met 22) door gebruik te maken van meer geheugen (voor compressie en decompression):

`zstd --ultra -{{level}} {{pad/naar/bestand}}`
