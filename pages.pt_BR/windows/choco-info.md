# choco info

> Exibir informações detalhadas de um pacote com Chocolatey.
> Mais informações: <https://chocolatey.org/docs/commands-info>.

- Exibir informações sobre um pacote específico:

`choco info {{pacote}}`

- Exibir informação para um pacote local:

`choco info {{pacote}} --local-only`

- Especificar uma fonte personalizada para receber as informações de um pacote:

`choco info {{pacote}} --source {{url_da_fonte|apelido}}`

- Fornecer um nome e uma senha para autenticação:

`choco info {{pacote}} --user {{apelido}} --password {{senha}}`
