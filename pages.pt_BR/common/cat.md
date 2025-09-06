# cat

> Exibe e concatena o conteúdo de arquivos.
> Mais informações: <https://manned.org/cat.1posix>.

- Exibe o conteúdo de um arquivo na `stdout`:

`cat {{caminho/para/arquivo}}`

- Concatena o conteúdo de vários arquivos em um arquivo de saída:

`cat {{caminho/para/arquivo1 caminho/para/arquivo2 ...}} > {{caminho/para/arquivo_de_saída}}`

- Anexa o conteúdo de vários arquivos ao final de um arquivo de saída:

`cat {{caminho/para/arquivo1 caminho/para/arquivo2 ...}} >> {{caminho/para/arquivo_de_saída}}`

- Copia o conteúdo de um arquivo em um arquivo de saída sem armazenamento em buffer:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Escreve a `stdin` em um arquivo:

`cat - > {{caminho/para/arquivo}}`
