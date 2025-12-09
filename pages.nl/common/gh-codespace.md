# gh codespace

> Verbind en beheer je codespaces in GitHub.
> Meer informatie: <https://cli.github.com/manual/gh_codespace>.

- Maak interactief een codespace aan in GitHub:

`gh {{[cs|codespace]}} create`

- Toon alle beschikbare codespaces:

`gh {{[cs|codespace]}} {{[ls|list]}}`

- Verbind interactief met een codespace via SSH:

`gh {{[cs|codespace]}} ssh`

- Kopieer interactief een specifiek bestand naar de codespace:

`gh {{[cs|codespace]}} cp {{pad/naar/bron_file}} remote:{{pad/naar/remote_bestand}}`

- Toon interactief de poorten van een codespace:

`gh {{[cs|codespace]}} ports`

- Toon interactief de logs van een codespace:

`gh {{[cs|codespace]}} logs`

- Verwijder interactief een codespace:

`gh {{[cs|codespace]}} delete`

- Toon de help voor een subcommando:

`gh {{[cs|codespace]}} {{code|cp|create|delete|edit|...}} {{[-h|--help]}}`
