# du

> Uso de disco: estima e sumariza o uso de espaço em disco de arquivos e diretórios.
> Mais informações: <https://www.gnu.org/software/coreutils/du>.

- Lista os tamanhos dos diretórios e qualquer subdiretório, em uma unidade de tamanho (B/KiB/MiB):

`du -{{b|k|m}} {{caminho/para/diretorio}}`

- Lista os tamanhos dos diretórios e subdiretórios, em tamanho legívell por humanos (isto é seleciona automaticamente a unidade de tamanho apropriada para o tamanho):

`du -h {{caminho/para/diretorio}}`

- Exibe o tamanho de um único diretório, em tamanho legível por humanos:

`du -sh {{caminho/para/diretorio}}`

- Lista em tamanho legível por humanos todos os arquivos e diretórios dentro de um diretório:

`du -ah {{caminho/para/diretorio}}`

- Lista em tamanho legível por humanos, até o nível N de profundidade um diretório e subdiretórios:

`du -h --max-depth=N {{caminho/para/diretorio}}`

- Lista em tamanho legível por humanos todos os arquivos `.jpg` dos subdiretórios do diretório atual, e exibe o total cumulativo no final:

`du -ch {{*/*.jpg}}`
