# nvim

> Neovim, um editor de texto para programadores baseado no Vim, oferece vários modos para diferentes tipos de manipulação de texto.
> Pressionar`i` no modo normal entra no modo de inserção. `<Esc>` retorna ao modo normal, que não permite a inserção regular de texto.
> Veja também `vim`, `vimtutor`, `vimdiff`.
> Mais informações: <https://neovim.io>.

- Abrir um arquivo:

`nvim {{caminho/para/arquivo}}`

- Entrar no modo de edição de texto (mode de inserção):

`<Esc>i`

- Copiar ("puxar") ou cortar ("apagar") a linha atual (cole-a com `P`):

`<Esc>{{yy|dd}}`

- Entrar no modo normal e desfazer a última operação:

`<Esc>u`

- Procurar por um padrão em um arquivo (pressione `n`/ `N` para ir para a próxima/prévia correspondência):

`<Esc>/{{padrão_procurado}}<Enter>`

- Executar uma substituição de expressão regular em todo o arquivo:

`<Esc>:%s/{{expressão_regular}}/{{substituição}}/g<Enter>`

- Entrar no modo normal, salvar (gravar) o arquivo e sair:

`<Esc>:wq<Enter>`

- Sair sem salvar:

`<Esc>:q!<Enter>`
