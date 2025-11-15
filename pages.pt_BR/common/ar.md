# ar

> Cria, modifica e extrai de arquivos Unix. Normalmente usado para bibliotecas estáticas (`.a`) e pacotes Debian (`.deb`).
> Veja também: `tar`.
> Mais informações: <https://manned.org/ar>.

- Descompacta todos os membros de um arquivo compactado:

`ar x {{caminho/para/arquivo.a}}`

- Lista o conteúdo em um arquivo compactado específico:

`ar t {{caminho/para/arquivo.ar}}`

- Substitui ou adiciona arquivos específicos para um arquivo compactado:

`ar r {{caminho/para/arquivo.deb}} {{caminho/para/binário-debian caminho/para/control.tar.gz caminho/para/data.tar.xz ...}}`

- Insere um índice de arquivos objetos (equivalente a usar `ranlib`):

`ar s {{caminho/para/arquivo.a}}`

- Cria um arquivo compactado com arquivos específicos, acompanhado por um índice de arquivo objeto:

`ar rs {{caminho/para/arquivo.a}} {{caminho/para/arquivo1.o caminho/para/arquivo2.o ...}}`
