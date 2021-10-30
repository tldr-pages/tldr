# choco uninstall

> Desinstalar um pacote ou mais com Chocolatey.
> Mais informações: <https://chocolatey.org/docs/commands-uninstall>.

- Desinstalar um pacote ou mais separado por espaços:

`choco uninstall {{pacote(s)}}`

- Desinstalar uma versão específica de um pacote:

`choco uninstall {{pacote}} --version {{versão}}`

- Confirmar todos prompts automaticamente:

`choco uninstall {{pacote}} --yes`

- Remover todas dependências ao desinstalar:

`choco uninstall {{pacote}} --remove-dependencies`

- Desinstalar todos os pacotes:

`choco uninstall all`
