# gh config

> Modificați configurația pentru GitHub cli.
> Mai multe informaţii: <https://cli.github.com/manual/gh_config>

- Afișați ce protocol Git este utilizat:

`gh config get git_protocol`

- Setați protocolul la SSH:

`gh config set git_protocol {{ssh}}`

- Utilizați `delta` în modul side-by-side ca pager implicit pentru toate comenzile `gh`:

`gh config set pager '{{delta --side-by-side}}'`

- Setați editorul de text la Vim:

`gh config set editor {{vim}}`

- Resetați la editorul de text implicit:

`gh config set editor {{""}}`

- Dezactivați solicitările interactive:

`gh config set prompt {{disabled}}`

- Setați o valoare specifică de configurare:

`gh config set {{key}} {{value}}`
