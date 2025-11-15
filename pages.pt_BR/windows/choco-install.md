# choco install

> Instalar um pacote ou mais com Chocolatey.
> Mais informações: <https://chocolatey.org/docs/commands-install>.

- Instala um ou mais pacotes separado por espaço:

`choco install {{pacote(s)}}`

- Instala pacotes a partir de um aquivo de configuração personalizado:

`choco install {{caminho/para/pacotes.config}}`

- Instala um arquivo específico `nuspec` ou `nupkg`:

`choco install {{caminho/para/arquivo}}`

- Instala uma versão específica de um pacote:

`choco install {{pacote}} --version {{versão}}`

- Permite a instalação de múltiplas versões de um pacote:

`choco install {{pacote}} --allow-multiple`

- Confirma todos prompts automaticamente:

`choco install {{pacote}} --yes`

- Especifica uma fonte personalizada para receber pacotes:

`choco install {{pacote}} --source {{url_do_pacote|apelido}}`

- Fornece um nome e uma senha para autenticação:

`choco install {{pacote}} --user {{usuario}} --password {{senha}}`
