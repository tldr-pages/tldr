# bat

> Imprime e concatena arquivos.
> Um clone do `cat` com realce de sintaxe e integração com Git.
> Mais informações: <https://github.com/sharkdp/bat>.

- Imprime o conteúdo de um arquivo para a saída padrão:

`bat {{arquivo}}`

- Concatena o conteúdo de vários arquivos em um arquivo destino:

`bat {{arquivo1}} {{arquivo2}} > {{arquivo_destino}}`

- Acrescenta o conteúdo de vários arquivos ao final de um arquivo destino:

`bat {{arquivo1}} {{arquivo2}} >> {{arquivo_destino}}`

- Numera todas as linhas de saída:

`bat -n {{arquivo}}`

- Realça a sintaxe de um arquivo JSON:

`bat --language json {{arquivo.json}}`

- Mostra todas as linguagens suportadas:

`bat --list-languages`
