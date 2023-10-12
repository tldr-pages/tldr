# nvim

> Neovim, um editor de texto para programadores baseado no Vim, oferece vários modos para diferentes tipos de manipulação de texto.
> Pressionar`i` no modo normal entra no modo de inserção. `<Esc>` retorna ao modo normal, que não permite a inserção regular de texto.
> Veja também `vim`, `vimtutor`, `vimdiff`.
> Mais informações: <https://neovim.io>.

- Abre um arquivo:

`nvim {{caminho/para/arquivo}}`

- Entra no modo de edição de texto (mode de inserção):

`<Esc>i`

- Copia ("yank") ou recorta ("delete") a linha atual (cole-a com `P`):

`<Esc>{{yy|dd}}`

- Entra no modo normal e desfaz a última operação:

`<Esc>u`

- Procura por um padrão em um arquivo (pressione `n`/ `N` para ir para a próxima/prévia correspondência):

`<Esc>/{{padrão_procurado}}<Enter>`

- Executa uma substituição de expressão regular em todo o arquivo:

`<Esc>:%s/{{expressão_regular}}/{{substituição}}/g<Enter>`

- Entra no modo normal, salva (grava) o arquivo e sai:

`<Esc>:wq<Enter>`

- Sai sem salvar:

`<Esc>:q!<Enter>`
