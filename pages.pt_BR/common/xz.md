# xz

> Compactar ou descompactar arquivos XZ ou LZMA.
> Mais informações: <https://manned.org/xz>.

- Compacta um arquivo no formato xz:

`xz {{caminho/para/arquivo}}`

- Descompacta um arquivo no formato xz:

`xz {{[-d|--decompress]}} {{caminho/para/arquivo.xz}}`

- Compacta um arquivo no formato LZMA:

`xz {{[-F|--format]}} lzma {{caminho/para/arquivo}}`

- Descompacta um arquivo no formato LZMA:

`xz {{[-d|--decompress]}} {{[-F|--format]}} lzma {{caminho/para/arquivo.lzma}}`

- Descompacta um arquivo e escrever a saída no terminal (implica `--keep`):

`xz {{[-d|--decompress]}} {{[-c|--stdout]}} {{caminho/para/arquivo.xz}}`

- Compacta um arquivo sem apagar o arquivo original:

`xz {{[-k|--keep]}} {{caminho/para/arquivo}}`

- Compacta um arquivo utilizando a compactação mais rápida:

`xz -0 {{caminho/para/arquivo}}`

- Compacta um arquivo utilizando a compactação mais eficiente:

`xz -9 {{caminho/para/arquivo}}`
