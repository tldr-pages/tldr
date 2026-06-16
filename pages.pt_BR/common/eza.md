# eza

> Substituto moderno e mantido para o `ls`, construída sobre o `exa`.
> Mais informações: <https://github.com/eza-community/eza>.

- Lista os arquivos um por linha:

`eza {{[-1|--oneline]}}`

- Lista todos os arquivos, incluindo arquivos ocultos:

`eza {{[-a|--all]}}`

- Lista no formato longo (permissões, propriedade, tamanho e data de modificação) de todos os arquivos:

`eza {{[-al|--all --long]}}`

- Lista os arquivos com os maiores no topo:

`eza {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Exibe uma árvore de arquivos com três níveis de profundidade:

`eza {{[-lT|--long --tree]}} {{[-L|--level]}} {{3}}`

- Lista os arquivos ordenados pela data de modificação (mais antigos primeiro):

`eza {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- Lista os arquivos com seus cabeçalhos, ícones e status do Git:

`eza {{[-lh|--long --header]}} --icons --git`

- Não lista os arquivos mencionados em `.gitignore`:

`eza --git-ignore`
