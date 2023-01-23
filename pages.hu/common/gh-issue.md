# gh issue

> GitHub problémák kezelése a parancssorból. További információ: <https://cli.github.com/manual/gh_issue>.

- Egy adott issue megjelenítése:

`gh issue view {{issue_number}}`

- Egy adott issue megjelenítése az alapértelmezett webböngészőben:

`gh issue view {{issue_number}} --web`

- Új issue létrehozása az alapértelmezett webböngészőben:

`gh issue create --web`

- Az utolsó 10 issue listázása a `bug` címkével:

`gh issue list --limit {{10}} --label "{{bug}}"`

- Egy adott felhasználó által készített lezárt kérdések listázása:

`gh issue list --state closed --author {{username}}`

- A felhasználó számára releváns kérdések állapotának megjelenítése egy adott tárolóban:

`gh issue status --repo {{owner}}/{{repository}}`

- Egy adott issue újranyitása:

`gh issue reopen {{issue_number}}`
