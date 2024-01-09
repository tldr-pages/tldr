# xz

> Compactar ou descompactar arquivos com a extensão .xz ou .lzma.
> Mais informações: <https://manned.org/xz>.

- Compacta um arquivo no formato xz:

`xz {{caminho/para/arquivo}}`

- Descompacta um arquivo no formato xz:

`xz --decompress {{caminho/para/arquivo.xz}}`

- Compacta um arquivo no formato lzma:

`xz --format=lzma {{caminho/para/arquivo}}`

- Descompacta um arquivo no formato lzma:

`xz --decompress --format=lzma {{caminho/para/arquivo.lzma}}`

- Descompacta um arquivo e escrever a saída no terminal (implica `--keep`):

`xz --decompress --stdout {{caminho/para/arquivo.xz}}`

- Compacta um arquivo sem apagar o arquivo original:

`xz --keep {{caminho/para/arquivo}}`

- Compacta um arquivo utilizando a compactação mais rápida:

`xz -0 {{caminho/para/arquivo}}`

- Compacta um arquivo utilizando a compactação mais eficiente:

`xz -9 {{caminho/para/arquivo}}`
