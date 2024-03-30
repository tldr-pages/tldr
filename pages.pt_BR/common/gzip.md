# gzip

> Compacta/descompacta arquivos com compressão gzip (LZ77).
> Mais informações: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Compacta um arquivo, substituindo-o por uma versão compactada gzip:

`gzip {{arquivo.ext}}`

- Descompacta um arquivo, substituindo-o pela versão não compactada original:

`gzip -d {{arquivo.ext}}.gz`

- Compacta um arquivo, mantendo o arquivo original:

`gzip --keep {{arquivo.ext}}`

- Compacta um arquivo definindo o nome do arquivo de saída:

`gzip -c {{arquivo.ext}} > {{arquivo_compactado.ext.gz}}`

- Descompacta um arquivo gzip definindo o nome do arquivo de saída:

`gzip -c -d {{arquivo.ext}}.gz > {{arquivo_descompactado.ext}}`

- Especifica o nível de compactação. 1=mais rápido (pior), 9=mais lendo 9melhor, o nível padrão é 6:

`gzip -9 -c {{arquivo.ext}} > {{arquivo_compactado.ext.gz}}`
