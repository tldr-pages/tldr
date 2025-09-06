# choco uninstall

> Desinstalar um pacote ou mais com Chocolatey.
> Mais informações: <https://chocolatey.org/docs/commands-uninstall>.

- Desinstala um pacote ou mais separado por espaços:

`choco uninstall {{pacote(s)}}`

- Desinstala uma versão específica de um pacote:

`choco uninstall {{pacote}} --version {{versão}}`

- Confirma todos prompts automaticamente:

`choco uninstall {{pacote}} --yes`

- Remove todas dependências ao desinstalar:

`choco uninstall {{pacote}} --remove-dependencies`

- Desinstala todos os pacotes:

`choco uninstall all`
