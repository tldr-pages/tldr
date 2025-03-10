# gzip

> Compacta/descompacta arquivos com compressão gzip (LZ77).
> Mais informações: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Compacta um arquivo, substituindo-o por uma versão compactada gzip:

`gzip {{caminho_para_arquivo}}`

- Descompacta um arquivo, substituindo-o pela versão descompactada original:

`gzip {{[-d|--decompress]}} {{caminho/para/arquivo.gz}}`

- Compacta um arquivo, mantendo o arquivo original:

`gzip {{[-k|--keep]}} {{caminho/para/arquivo}}`

- Compacta um arquivo definindo o nome do arquivo de saída:

`gzip {{[-c|--stdout]}} {{caminho/para/arquivo}} > {{caminho/para/arquivo_compactado.gz}}`

- Descompacta um arquivo gzip definindo o nome do arquivo de saída:

`gzip {{[-c|--stdout]}} {{[-d|--decompress]}} {{caminho/para/arquivo.gz}} > {{caminho/para/arquivo_descompactado}}`

- Especifica o nível de compactação. 1 é o mais rápido (baixa compressão), 9 é o mais lento (baixa compressão), o nível padrão é 6:

`gzip -{{1..9}} {{[-c|--stdout]}} {{caminho/para/arquivo}} > {{caminho/para/arquivo_compactado.gz}}`

- Mostra o nome e o percentual de redução para cada arquivo comprimido ou descomprimido:

`gzip {{[-v|--verbose]}} {{[-d|--decompress]}} {{caminho/para/arquivo.gz}}`
