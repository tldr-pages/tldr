# gh issue

> Gestionați problemele GitHub din linia de comandă.
> Mai multe informaţii: <https://cli.github.com/manual/gh_issue>

- Tipăriţi problema:

`gh issue view {{issue_number}}`

- Creați o nouă problemă în browserul web:

`gh issue create --web`

- Listează ultimele 10 emisiuni cu eticheta „bug”:

`gh issue list --limit {{10}} --label "{{bug}}"`

- Lista problemelor închise făcute de un anumit utilizator:

`gh issue list --state closed --author {{username}}`

- Afișați starea problemelor relevante pentru utilizator, într-un anumit depozit:

`gh issue status --repo {{owner}}/{{repository}}`

- Redeschide o problemă:

`gh issue reopen {{issue_number}}`
