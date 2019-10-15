# bat

> Imprimir e concatenar arquivos.
> Um clone de `cat` com destaque de sintaxe e integraço com Git. 

- Imprimir os conteúdos de um arquivo para a standard output:

`bat {{arquivo}}`

- Concatenar vários arquivos para um arquivo de destino:

`bat {{arquivo1}} {{arquivo2}} > {{arquivo_destino}}`

- Concatenar vários arquivos para um arquivo de destino:

`bat {{arquivo1}} {{arquivo2}} >> {{arquivo_destino}}`

- Numerar todas as linhas do output:

`bat -n {{arquivo}}`

- Destaque de sintaxe em um arquivo de json:

`bat --language json {{arquivo.json}}`

- Mostrar todas as linguagens suportadas:

`bat --list-languages`
