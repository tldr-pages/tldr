# git

> Gedistribueerd versiebeheersysteem.
> Sommige subcommando's zoals `commit`, `add`, `branch`, `checkout`, `push`, etc. hebben hun eigen documentatie.
> Meer informatie: <https://git-scm.com/docs/git>.

- Voer een Git-subcommando uit:

`git {{subcommando}}`

- Voer een Git-subcommando uit op een aangepast repository-rootpad:

`git -C {{pad/naar/repo}} {{subcommando}}`

- Voer een Git-subcommando met een gegeven configuratieset:

`git -c '{{config.key}}={{waarde}}' {{subcommando}}`

- Toon de algemene help:

`git {{[-h|--help]}}`

- Toon de help van een specifiek subcommando (zoals `clone`, `add`, `push`, `log`, enz.):

`git help {{subcommando}}`

- Toon de versie:

`git {{[-v|--version]}}`
