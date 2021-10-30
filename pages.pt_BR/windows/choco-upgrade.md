# choco upgrade

> Atualizar um ou mais pacotes com Chocolatey.
> Mais informações: <https://chocolatey.org/docs/commands-upgrade>.

- Atualizar um ou mais pacotes separados por espaço:

`choco upgrade {{pacote(s)}}`

- Atualizar para uma versão específica de um pacote:

`choco upgrade {{pacote}} --version {{versão}}`

- Atualizar todos pacotes:

`choco upgrade all`

- Atualizar todos os pacotes, exceto os especificados separados por virgula:

`choco upgrade all --except "{{pacote(s)}}"`

- Confirmar todos prompts automaticamente:

`choco upgrade {{pacote}} --yes`

- Especifique uma fonte personalizada para receber pacotes:

`choco upgrade {{pacote}} --source {{url_do_pacote|apelido}}`

- Fornecer um nome e uma senha para autenticação:

`choco upgrade {{pacote}} --user {{usuário}} --password {{senha}}`
