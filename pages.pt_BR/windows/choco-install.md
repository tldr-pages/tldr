# choco install

> Instalar um pacote ou mais com Chocolatey.
> Mais informação: <https://chocolatey.org/docs/commands-install>.

- Instalar um ou mais pacotes separado por espaço:

`choco install {{package(s)}}`

- Instalar pacotes a partir de um aquivo de configuração personalizado:

`choco install {{path/to/packages.config}}`

- Instalar um arquivo específico "nuspec" ou "nupkg":

`choco install {{path/to/file}}`

- Instalar uma versão específica de um pacote:

`choco install {{package}} --version {{version}}`

- Permitir a instalação de múltiplas versões de um pacote:

`choco install {{package}} --allow-multiple`

- Confirmar todos prompts automaticamente:

`choco install {{package}} --yes`

- Especificar uma fonte personalizada para receber pacotes:

`choco install {{package}} --source {{source_url|alias}}`

- Fornecer um nome e uma senha para autenticação:

`choco install {{package}} --user {{username}} --password {{password}}`
