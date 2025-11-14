# bzip2

> Um compressor de arquivos que utiliza o algoritmo Burrows-Wheeler.
> Veja também: `bzcat`, `bunzip2`, `bzip2recover`.
> Mais informações: <https://manned.org/bzip2>.

- Compacta um arquivo:

`bzip2 {{arquivo}}`

- Descompacta um arquivo:

`bzip2 {{[-d|--decompress]}} {{arquivo_compactado.bz2}}`

- Descompacta um arquivo exibindo o conteúdo no terminal:

`bzip2 {{[-dc|--decompress --stdout]}} {{arquivo_compactado.bz2}}`

- Testa a integridade de cada arquivo dentro do arquivo compactado:

`bzip2 {{[-t|--test]}} {{caminho/para/arquivo_compactado.bz2}}`

- Exibe a taxa de compressão para cada arquivo processado com informações detalhadas:

`bzip2 {{[-v|--verbose]}} {{caminho/para/arquivos_compactados.bz2}}`

- Descompacta um arquivo sobrescrevendo arquivos existentes:

`bzip2 {{[-f|--force]}} {{caminho/para/arquivo_compactado.bz2}}`

- Exibe ajuda:

`bzip2 {{[-h|--help]}}`
