# bat

> Imprimir e concatenar arquivos.
> Um clone do `cat` com realce de sintaxe e integração com Git.
> Mais informações: <https://github.com/sharkdp/bat>.

- Imprimir o conteúdo de um arquivo para a saída padrão:

`bat {{arquivo}}`

- Concatenar vários arquivos em um arquivo de destino:

`bat {{caminho/para/arquivo1}} {{caminho/para/arquivo2}} > {{caminho/para/arquivo_destino}}`

- Numerar todas as linhas do output:

`bat -n {{caminho/para/arquivo}}`

- Realçar a sintaxe em um arquivo JSON:

`bat --language json {{caminho/para/arquivo.json}}`

- Mostrar todas as linguagens suportadas:

`bat --list-languages`
