# bzip2

> Um compressor de arquivos que utiliza o algoritmo Burrows–Wheeler.
> Mais informações: <https://manned.org/bzip2>.

- Compacta um arquivo:

`bzip2 {{arquivo}}`

- Descompacta um arquivo:

`bzip2 -d {{arquivo_compactado.bz2}}`

- Descompacta um arquivo exibindo o conteúdo no terminal:

`bzip2 -dc {{arquivo_compactado.bz2}}`

- Testa a integridade de cada arquivo dentro do arquivo compactado:

`bzip2 --test {{caminho/para/arquivo_compactado.bz2}}`

- Exibe a taxa de compressão para cada arquivo processado com informações detalhadas:

`bzip2 --verbose {{caminho/para/arquivos_compactados.bz2}}`

- Descompacta um arquivo sobrescrevendo arquivos existentes:

`bzip2 --force {{caminho/para/arquivo_compactado.bz2}}`

- Exibe ajuda:

`bzip2 -h`
