# glab

> Zökkenőmentes munka a GitLabbal a parancssorból. Néhány alparancsnak, mint például a `glab config`, saját használati dokumentációja van. További információ: <https://github.com/profclems/glab>.

- GitLab tárolóhely klónozása helyben:

`glab repo clone {{owner}}/{{repository}}`

- Új kiadás létrehozása:

`glab issue create`

- Az aktuális adattár nyitott kérdéseinek megtekintése és szűrése:

`glab issue list`

- Egy issue megtekintése az alapértelmezett böngészőben:

`glab issue view --web {{issue_number}}`

- Egyesítési kérelem létrehozása:

`glab mr create`

- Egy pull request megtekintése az alapértelmezett böngészőben:

`glab mr view --web {{pr_number}}`

- Egy adott pull request helyi megtekintése:

`glab mr checkout {{pr_number}}`
