# gh codespace

> Conecta e gerencia seus codespaces no GitHub.
> Mais informações: <https://cli.github.com/manual/gh_codespace>.

- Cria um codespace no GitHub interativamente:

`gh {{[cs|codespace]}} create`

- Lista todos os codespaces disponíveis:

`gh {{[cs|codespace]}} {{[ls|list]}}`

- Conecta a um codespace via SSH interativamente:

`gh {{[cs|codespace]}} ssh`

- Transfere um arquivo específico para um codespace interativamente:

`gh {{[cs|codespace]}} cp {{caminho/para/arquivo_fonte}} remote:{{caminho/para/arquivo_remoto}}`

- Lista os ports de um codespace interativamente:

`gh {{[cs|codespace]}} ports`

- Exibe os registros de um codespace interativamente:

`gh {{[cs|codespace]}} logs`

- Exclui um codespace interativamente:

`gh {{[cs|codespace]}} delete`

- Exibe ajuda para um subcomando:

`gh {{[cs|codespace]}} {{code|cp|create|delete|edit|...}} {{[-h|--help]}}`
