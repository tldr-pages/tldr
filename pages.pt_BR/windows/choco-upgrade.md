# choco upgrade

> Atualizar um ou mais pacotes com Chocolatey.
> Mais informações: <https://chocolatey.org/docs/commands-upgrade>.

- Atualiza um ou mais pacotes separados por espaço:

`choco upgrade {{pacote(s)}}`

- Atualiza para uma versão específica de um pacote:

`choco upgrade {{pacote}} --version {{versão}}`

- Atualiza todos pacotes:

`choco upgrade all`

- Atualiza todos os pacotes, exceto os especificados separados por virgula:

`choco upgrade all --except "{{pacote(s)}}"`

- Confirma todos os prompts automaticamente:

`choco upgrade {{pacote}} --yes`

- Especifique uma fonte personalizada para receber pacotes:

`choco upgrade {{pacote}} --source {{url_do_pacote|apelido}}`

- Fornece um nome e uma senha para autenticação:

`choco upgrade {{pacote}} --user {{usuário}} --password {{senha}}`
