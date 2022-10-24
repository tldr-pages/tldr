# vim

> Vim (Vi IMproved), é um editor de texto em linha de comando, que fornece muitos modos para diferentes tipos de manipulação de texto.
> Apertando `i` no modo normal entra em modo insert (inserir). Apertando `<Esc>` volta para o modo normal, que permite o uso dos comandos do Vim.
> Mais informações: <https://www.vim.org>.

- Abre um arquivo:

`vim {{caminho/para/arquivo}}`

- Abre um arquivo em um número da linha específica:

`vim +{{número_da_linha}} {{caminho/para/arquivo}}`

- Abre o manual do Vim em visualização:

`:help<Enter>`

- Salva e sai do arquivo atual:

`:wq<Enter>`

- Entra em modo normal e desfaz a última operação:

`<ESC>u`

- Procura por um sequência padrão dentro de um arquivo (aperte `n`/`N` para ir para próxima/anterior sequência padrão):

`/{{sequência_padrão_procurada}}<Enter>`

- Executa uma substituição por expressão regular no arquivo todo:

`:%s/{{expressão_regular}}/{{substituição}}/g<Enter>`

- Mostra os números das linhas:

`:set nu<Enter>`
