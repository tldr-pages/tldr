# du

> Uso do disco: estima e sumariza arquivos e diretórios do uso em espaço em disco.
> Mais informações: <https://www.gnu.org/software/coreutils/du>.

- Lista  os tamanhos dos diretórios e qualquer subdiretório, em uma unidade de tamanho (B/KiB/MiB):

`du -{{b|k|m}} {{caminho/para/diretório}}`

- Lista os tamanhos dos diretórios e subdiretórios, em uma forma compreensível por humanos (isto é seleciona automaticamente a unidade de tamanho apropriada para o tamanho):

`du -h {{caminho/para/diretório}}`

- Exibe o tamanho de um diretório único, em uma unidade compreensível por humanos:

`du -sh {{caminho/para/diretório}}`

- Lista em uma forma compreensível por humanos de um diretório todos os arquivos e diretórios dentro dele:

`du -ah {{caminho/para/diretório}}`

- Lista em uma forma compreensível por humanos de um diretório e subdiretórios, até o nível N de profundidade:

`du -h --max-depth=N {{caminho/para/diretório}}`

- Lista em uma forma compreensível por humanos todos os arquivos `.jpg` dos subdiretórios do diretório atual, e exibe o total cumulativo no final:

`du -ch {{*/*.jpg}}`
