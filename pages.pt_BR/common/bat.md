# bat

> Imprime e concatena arquivos.
> Um clone do `cat` com realce de sintaxe e integração com Git.
> Mais informações: <https://github.com/sharkdp/bat>.

- Imprime o conteúdo formatado de um arquivo para a saída padrão (stdout):

`bat {{/caminho/para/arquivo}}`

- Concatena o conteúdo de vários arquivos em um arquivo destino:

`bat {{/caminho/para/arquivo1 /caminho/para/arquivo2 ...}} > {{/caminho/para/arquivo_destino}}`

- Remove estilizacão e desabilita páginação (`--style plain` pode ser substituído por `-p`, ou ambas as opções com `-pp`):

`bat --style plain --pager never {{/caminho/para/arquivo}}`

- Destaca uma linha específica ou um intervalo de linhas com uma cor de fundo diferente:

`bat {{[-H|--highlight-line]}} {{10|5:10|:10|10:|10:+5}} {{/caminho/para/arquivo}}`

- Mostra caracteres não imprimíveis como espaço, tab ou nova linha:

`bat {{[-A|--show-all]}} {{/caminho/para/arquivo}}`

- Remove toda estilizacão exceto os números das linhas no arquivo de saída:

`bat {{[-n|--number]}} {{/caminho/para/arquivo}}`

- Realça a sintaxe de um arquivo ao definir explicitamente a linguagem (e.g. JSON):

`bat {{[-l|--language]}} json {{/caminho/para/arquivo.json}}`

- Mostra todas as linguagens suportadas:

`bat {{[-L|--list-languages]}}`
