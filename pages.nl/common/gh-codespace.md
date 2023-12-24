# gh codespace

> Verbind en beheer je codespaces in GitHub.
> Meer informatie: <https://cli.github.com/manual/gh_codespace>.

- Maak interactief een codespace aan in GitHub:

`gh codespace create`

- Toon alle beschikbare codespaces:

`gh codespace list`

- Verbind interactief met een codespace via SSH:

`gh codespace ssh`

- Kopieer interactief een specifiek bestand naar de codespace:

`gh codespace cp {{pad/naar/bron_file}} remote:{{pad/naar/remote_bestand}}`

- Toon interactief de poorten van een codespace:

`gh codespace ports`

- Toon interactief de logs van een codespace:

`gh codespace logs`

- Verwijder interactief een codespace:

`gh codespace delete`

- Toon hulp voor een subcommando:

`gh codespace {{code|cp|create|delete|edit|...}} --help`
