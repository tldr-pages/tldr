# xz

> Compactar ou descompactar arquivos com a extensão .xz ou .lzma.

- Compactar um arquivo:

`xz {{arquivo}}`

- Descompactar um arquivo:

`xz -d {{arquivo.xz}}`

- Descompactar um arquivo e escrever a saída no terminal:

`xz -dc {{arquivo.xz}}`

- Compactar um arquivo sem apagar o arquivo original:

`xz -k {{arquivo}}`

- Compactar um arquivo utilizando a compactação mais rápida:

`xz -0 {{arquivo}}`

- Compactar um arquivo utilizando a compactação mais eficiente:

`xz -9 {{arquivo}}`
