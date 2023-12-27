# xz

> Compactar ou descompactar arquivos com a extensão .xz ou .lzma.
> Mais informações: <https://manned.org/xz>.

- Compacta um arquivo no formato xz:

`xz {{arquivo}}`

- Descompacta um arquivo no formato xz:

`xz -d {{arquivo.xz}}`

- Compacta um arquivo no formato lzma:

`xz --format=lzma {{arquivo}}`

- Descompacta um arquivo no formato lzma:

`xz -d --format=lzma {{arquivo.lzma}}`

- Descompacta um arquivo e escrever a saída no terminal:

`xz -dc {{arquivo.xz}}`

- Compacta um arquivo sem apagar o arquivo original:

`xz -k {{arquivo}}`

- Compacta um arquivo utilizando a compactação mais rápida:

`xz -0 {{arquivo}}`

- Compacta um arquivo utilizando a compactação mais eficiente:

`xz -9 {{arquivo}}`
