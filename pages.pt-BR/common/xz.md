# xz

> Compactar ou descompactar arquivos com a extensão .xz ou .lzma.
> Mais informações: <https://tukaani.org/xz/format.html>.

- Compactar um arquivo no formato xz:

`xz {{arquivo}}`

- Descompactar um arquivo no formato xz:

`xz -d {{arquivo.xz}}`

- Compactar um arquivo no formato lzma:

`xz --format=lzma {{arquivo}}`

- Descompactar um arquivo no formato lzma:

`xz -d --format=lzma {{arquivo.lzma}}`

- Descompactar um arquivo e escrever a saída no terminal:

`xz -dc {{arquivo.xz}}`

- Compactar um arquivo sem apagar o arquivo original:

`xz -k {{arquivo}}`

- Compactar um arquivo utilizando a compactação mais rápida:

`xz -0 {{arquivo}}`

- Compactar um arquivo utilizando a compactação mais eficiente:

`xz -9 {{arquivo}}`
