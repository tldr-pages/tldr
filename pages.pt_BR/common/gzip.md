# gzip

> Ferramenta de compressão e descompressão de arquivos com formato gzip (LZ77).
> Mais informações: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Comprimir um arquivo substituindo o original por sua versão compactada:

`gzip {{arquivo.ext}}`

- Descomprimir um arquivo removendo o arquivo gzip:

`gzip --decompress {{arquivo.ext}}.gz`

- Comprimir um arquivo definindo o nível de máximo de compressão [9]:

`gzip -{{9}} {{arquivo.ext}}`

- Comprimir um arquivo mantendo o original:

`gzip --keep {{arquivo.ext}}`

- Descomprimir um arquivo mantendo o arquivo gzip:

`gzip --decompress --keep {{arquivo.ext}}.gz`

- Comprimir arquivo mantendo o original e definindo o nome do arquivo comprimido:

`gzip --to-stdout {{arquivo.ext}} > {{arquivo_comprimido.ext.gz}}`

- Descomprimir um arquivo mantendo o arquivo gzip e definindo o nome do arquivo descomprimido:

`gzip --decompress --to-stdout {{arquivo.ext}}.gz > {{arquivo_descomprimido.ext}}`
