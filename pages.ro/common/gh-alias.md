# gh alias

> Gestionarea aliasurilor de comandă GitHub CLI din linia de comandă.
> Mai multe informaţii: <https://cli.github.com/manual/gh_alias>

- Afișează ajutorul subcomenzii:

`gh alias`

- Lista tuturor aliasurilor `gh` este configurat sa foloseasca:

`gh alias list`

- Creați un alias de subcomandă `gh`:

`gh alias set {{pv}} '{{pr view}}'`

- Setați o comandă shell ca subcomandă `gh`:

`gh alias set --shell {{alias_name}} {{command}}`

- Ștergeți o comandă rapidă de comandă:

`gh alias delete {{alias_name}}`
