# daps

> DAPS é um programa de código aberto para transformar DocBook XML em formatos de saída como HTML ou PDF.
> Mais informações: <https://opensuse.github.io/daps/doc/index.html>.

- Verifica se um arquivo DocBook XML é válido:

`daps -d {{caminho/para/arquivo.xml}} validate`

- Converte um arquivo DocBook XML para PDF:

`daps -d {{caminho/para/arquivo.xml}} pdf`

- Converte um arquivo DocBook XML em um único arquivo HTML:

`daps -d {{caminho/para/arquivo.xml}} html --single`

- Exibe ajuda:

`daps --help`

- Exibe versão:

`daps --version`
