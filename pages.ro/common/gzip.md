# gzip

> Compresie/decompresie fişiere cu compresie gzip (LZ77).
> Mai multe informaţii: <https://www.gnu.org/software/gzip/manual/gzip.html>

- Comprimați un fișier, înlocuindu-l cu o versiune comprimată gzipped:

`gzip {{file.ext}}`

- Decomprima un fișier, înlocuindu-l cu versiunea originală necomprimată:

`gzip -d {{file.ext}}.gz`

- Comprimați un fișier, păstrând fișierul original:

`gzip --keep {{file.ext}}`

- Comprimați un fișier care specifică numele fișierului de ieșire:

`gzip -c {{file.ext}} > {{compressed_file.ext.gz}}`

- Decomprima un fișier gzipped specificând numele fișierului de ieșire:

`gzip -c -d {{file.ext}}.gz > {{uncompressed_file.ext}}`

- Specificați nivelul de compresie. 1=Cel mai rapid (cel mai rău), 9 = Cel mai lent (cel mai bun), Nivelul implicit este 6:

`gzip -9 -c {{file.ext}} > {{compressed_file.ext.gz}}`
