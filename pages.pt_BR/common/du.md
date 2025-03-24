# du

> Uso de disco: estima e sumariza o uso de espaço em disco de arquivos e diretórios.
> Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- Lista os tamanhos dos diretórios e qualquer subdiretório, em uma unidade de tamanho (B/KiB/MiB):

`du -{{b|k|m}} {{caminho/para/diretório}}`

- Lista os tamanhos dos diretórios e subdiretórios, em tamanho legível por humanos (isto é seleciona automaticamente a unidade de tamanho apropriada para o tamanho):

`du {{[-h|--human-readable]}} {{caminho/para/diretório}}`

- Exibe o tamanho de um único diretório, em tamanho legível por humanos:

`du {{[-sh|--summarize --human-readable]}} {{caminho/para/diretório}}`

- Lista em tamanho legível por humanos todos os arquivos e diretórios dentro de um diretório:

`du {{[-ah|--all --human-readable]}} {{caminho/para/diretório}}`

- Lista em tamanho legível por humanos, até o nível N de profundidade um diretório e subdiretórios:

`du {{[-h|--human-readable]}} {{[-d|--max-depth]}} N {{caminho/para/diretório}}`

- Lista em tamanho legível por humanos todos os arquivos `.jpg` dos subdiretórios do diretório atual, e exibe o total cumulativo no final:

`du {{[-ch|--total --human-readable]}} {{*/*.jpg}}`

- Lista todos os arquivos e diretórios (incluindo os ocultos) acima de um limite de tamanho (útil para invetigar o que está de fato ocupando o espaço):

`du {{[-ah|--all --human-readable]}} {{[-t|--threshold]}} {{1G|1024M|1048576K}} .[^.]* *`
