# choco info

> Exibir informações detalhadas de um pacote com Chocolatey.
> Mais informações: <https://docs.chocolatey.org/en-us/choco/commands/info/>.

- Exibe informações sobre um pacote específico:

`choco info {{pacote}}`

- Exibe informação para um pacote local:

`choco info {{pacote}} {{[-l|--local-only]}}`

- Especifica uma fonte personalizada para receber as informações de um pacote:

`choco info {{pacote}} {{[-s|--source]}} {{url_da_fonte|apelido}}`

- Fornece um nome e uma senha para autenticação:

`choco info {{pacote}} {{[-u|--user]}} {{apelido}} {{[-p|--password]}} {{senha}}`
