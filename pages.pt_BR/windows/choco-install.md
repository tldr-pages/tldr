# choco install

> Instalar um pacote ou mais com Chocolatey.
> Mais informações: <https://chocolatey.org/docs/commands-install>.

- Instalar um ou mais pacotes separado por espaço:

`choco install {{pacote(s)}}`

- Instalar pacotes a partir de um aquivo de configuração personalizado:

`choco install {{caminho/para/os/pacotes.config}}`

- Instalar um arquivo específico `nuspec` ou `nupkg`:

`choco install {{caminho/para/o/arquivo}}`

- Instalar uma versão específica de um pacote:

`choco install {{pacote}} --version {{versão}}`

- Permitir a instalação de múltiplas versões de um pacote:

`choco install {{pacote}} --allow-multiple`

- Confirmar todos prompts automaticamente:

`choco install {{pacote}} --yes`

- Especificar uma fonte personalizada para receber pacotes:

`choco install {{pacote}} --source {{url_do_pacote|apelido}}`

- Fornecer um nome e uma senha para autenticação:

`choco install {{pacote}} --user {{usuario}} --password {{senha}}`
