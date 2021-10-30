# choco list

> Exibir uma lista de pacotes com Chocolatey.
> Mais informações: <https://chocolatey.org/docs/commands-list>.

- Exibir todos pacotes disponíveis:

`choco list`

- Exibir todos pacotes instalados localmente:

`choco list --local-only`

- Exibir uma lista incluindo programas locais:

`choco list --include-programs`

- Exibir apenas pacotes aprovados:

`choco list --approved-only`

- Especificar uma fonte personalizada para exibir os pacotes:

`choco list --source {{url_da_fonte|apelido}}`

- Fornecer um nome e uma senha para autenticação:

`choco list --user {{usuário}} --password {{senha}}`
