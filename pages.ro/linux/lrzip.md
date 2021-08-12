# lrzip

> Un program mare de compresie a fișierelor.
> A se vedea, de asemenea, `lrunzip, `lrztar`, `lrzuntar`.

- Comprimați un fișier cu LZMA - compresie lentă, decompresie rapidă:

`lrzip {{filename}}`

- Comprimați un fișier cu BZIP2 - sol bun mijloc pentru compresie/viteză:

`lrzip -b {{filename}}`

- Comprimare cu ZPAQ - compresie extremă, dar foarte lent:

`lrzip -z {{filename}}`

- Comprimare cu LZO - compresie ușoară, decompresie extrem de rapidă:

`lrzip -l {{filename}}`

- Comprimați un fișier și o parolă protejați/criptați-l:

`lrzip -e {{filename}}`

- Suprascrie numărul de fire de procesor pentru a utiliza:

`lrzip -p {{8}} {{filename}}`
