# cat

> Imprime e concatena arquivos.
> Mais informações: <https://www.gnu.org/software/coreutils/cat>.

- Imprime o conteúdo de um arquivo na `stdout`:

`cat {{caminho/para/arquivo}}`

- Concatena vários arquivos em um arquivo de saída:

`cat {{caminho/para/arquivo1 caminho/para/arquivo2 ...}} > {{caminho/para/arquivo_de_saída}}`

- Anexa vários arquivos a um arquivo de saída:

`cat {{caminho/para/arquivo1 caminho/para/arquivo2 ...}} >> {{caminho/para/arquivo_de_saída}}`

- Escreve a `stdin` em um arquivo:

`cat - > {{caminho/para/arquivo}}`

- [n]umera todas as linhas de saída:

`cat -n {{caminho/para/arquivo}}`

- Exibe caracteres não imprimíveis e espaço em branco (com o prefixo `M-` se não for ASCII):

`cat -v -t -e {{caminho/para/arquivo}}`
