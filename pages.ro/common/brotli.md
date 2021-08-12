# Brotli

> Comprimare/decomprimare fișiere cu compresie brotli.
> Mai multe informaţii: <https://github.com/google/brotli>

- Comprimați un fișier, creând o versiune comprimată lângă fișier:

`brotli {{file.ext}}`

- Decomprima un fișier, creând o versiune necomprimată lângă fișier:

`brotli -d {{file.ext}}.br`

- Comprimați un fișier care specifică numele fișierului de ieșire:

`brotli {{file.ext}} -o {{compressed_file.ext.br}}`

- Decomprima un fişier brotli specificând numele fişierului de ieşire:

`brotli -d {{compressed_file.ext.br}} -o {{file.ext}}`

- Specificați nivelul de compresie. 1=Cel mai rapid (cel mai rău), 11 = Cel mai lent (cel mai bun):

`brotli -q {{11}} {{file.ext}} -o {{compressed_file.ext.br}}`
