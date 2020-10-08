# choco upgrade

> Atualizar um ou mais pacotes com Chocolatey.
> Mais informação: <https://chocolatey.org/docs/commands-upgrade>.

- Atualizar um ou mais pacotes separados por espaço:

`choco upgrade {{package(s)}}`

- Atualizar para uma versão específica de um pacote:

`choco upgrade {{package}} --version {{version}}`

- Atualizar todos pacotes:

`choco upgrade all`

- Atualizr todos, exceto os pacotes separados por vírgula especificados:

`choco upgrade all --except "{{package(s)}}"`

- Confirmar todos prompts automaticamente:

`choco upgrade {{package}} --yes`

- Especifique uma fonte personalizada para receber pacotes:

`choco upgrade {{package}} --source {{source_url|alias}}`

- Fornecer um nome e uma senha para autenticação:

`choco upgrade {{package}} --user {{username}} --password {{password}}`
