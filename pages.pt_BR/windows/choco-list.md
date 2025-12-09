# choco list

> Exibir uma lista de pacotes com Chocolatey.
> Mais informações: <https://chocolatey.org/docs/commands-list>.

- Exibe todos pacotes disponíveis:

`choco list`

- Exibe todos pacotes instalados localmente:

`choco list --local-only`

- Exibe uma lista incluindo programas locais:

`choco list --include-programs`

- Exibe apenas pacotes aprovados:

`choco list --approved-only`

- Especifica uma fonte personalizada para exibir os pacotes:

`choco list --source {{url_da_fonte|apelido}}`

- Fornece um nome e uma senha para autenticação:

`choco list --user {{usuário}} --password {{senha}}`
