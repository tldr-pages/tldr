# bat

> Imprimir e concatenar arquivos.
> Um clone de `cat` com destaque de sintaxe e integração com Git. 

- Imprimir os conteúdos de um arquivo para a standard output:

`bat {{arquivo}}`

- Concatenar vários arquivos para um arquivo de destino:

`bat {{caminho/para/arquivo1}} {{caminho/para/arquivo2}} > {{caminho/para/arquivo_destino}}`

- Numerar todas as linhas do output:

`bat -n {{caminho/para/arquivo}}`

- Ativar destaque de sintaxe em um arquivo json:

`bat --language json {{caminho/para/arquivo.json}}`

- Mostrar todas as linguagens suportadas:

`bat --list-languages`
