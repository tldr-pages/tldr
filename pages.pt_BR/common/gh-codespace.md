# gh codespace

> Conecta e gerencia seus codespaces no GitHub.
> Mais informações: <https://cli.github.com/manual/gh_codespace>.

- Cria um codespace no GitHub interativamente:

`gh codespace create`

- Lista todos os codespaces disponíveis:

`gh codespace list`

- Conecta a um codespace via SSH interativamente:

`gh codespace ssh`

- Transfere um arquivo específico para um codespace interativamente:

`gh codespace cp {{caminho/para/arquivo_fonte}} remote:{{caminho/para/arquivo_remoto}}`

- Lista os ports de um codespace interativamente:

`gh codespace ports`

- Exibe os registros de um codespace interativamente:

`gh codespace logs`

- Exclui um codespace interativamente:

`gh codespace delete`

- Exibe ajuda para um subcomando:

`gh codespace {{code|cp|create|delete|edit|...}} --help`
