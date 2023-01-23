# glab issue

> GitLab problémák kezelése a parancssorból. További információ: <https://glab.readthedocs.io/en/latest/issue>.

- Egy adott probléma megjelenítése:

`glab issue view {{issue_number}}`

- Egy adott issue megjelenítése az alapértelmezett webböngészőben:

`glab issue view {{issue_number}} --web`

- Új issue létrehozása az alapértelmezett webböngészőben:

`glab issue create --web`

- Az utolsó 10 issue listázása a `bug` címkével:

`glab issue list --per-page {{10}} --label "{{bug}}"`

- Egy adott felhasználó által készített lezárt kérdések listázása:

`glab issue list --closed --author {{username}}`

- Egy adott kérdés újranyitása:

`glab issue reopen {{issue_number}}`
