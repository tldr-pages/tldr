# gh

> Zökkenőmentes munka a GitHub-bal a parancssorból. Néhány alparancsnak, mint például a `gh config`, saját használati dokumentációja van. További információ: <https://cli.github.com/>.

- GitHub tárolóhely klónozása helyben:

`gh repo clone {{owner}}/{{repository}}`

- Új kiadás létrehozása:

`gh issue create`

- Az aktuális adattár nyitott kérdéseinek megtekintése és szűrése:

`gh issue list`

- Egy issue megtekintése az alapértelmezett webböngészőben:

`gh issue view --web {{issue_number}}`

- Pull-kérelem létrehozása:

`gh pr create`

- Pull-kérelem megtekintése az alapértelmezett webböngészőben:

`gh pr view --web {{pr_number}}`

- Egy adott pull request megtekintése helyben:

`gh pr checkout {{pr_number}}`

- Egy adattár pull-kérelmeinek állapotának ellenőrzése:

`gh pr status`
