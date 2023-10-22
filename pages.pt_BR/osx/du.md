# du

> Uso do Disco: estima e resume o uso do espaço de arquivos e diretórios.
> Mais informações: <https://ss64.com/osx/du.html>.

- Lista os tamanhos de um diretório e quaisquer subdiretórios, na unidade fornecida (KiB/MiB/GiB):

`du -{{k|m|g}} {{caminho/para/diretório}}`

- Lista os tamanhos de um diretório e quaisquer subdiretórios, em formato legível (ou seja, selecionando automaticamente a unidade apropriada para cada tamanho):

`du -h {{caminho/para/diretório}}`

- Exibe o tamanho de um único diretório, em unidades legíveis:

`du -sh {{caminho/para/diretório}}`

- Lista os tamanhos legíveis de um diretório e de todos os arquivos e diretórios dentro dele:

`du -ah {{caminho/para/diretório}}`

- Lista os tamanhos legíveis de um diretório e quaisquer subdiretórios, até N níveis de profundidade:

`du -h -d {{N}} {{caminho/para/diretório}}`

- Lista o tamanho legível de todos os arquivos `.jpg` nos subdiretórios do diretório atual e exibe um total cumulativo no final:

`du -ch {{*/*.jpg}}`
