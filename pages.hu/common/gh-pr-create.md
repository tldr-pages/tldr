# gh pr create

> GitHub pull requestek kezelése a parancssorból. További információ: <https://cli.github.com/manual/gh_pr_create>.

- Interaktívan hozzon létre egy pull requestet:

`gh pr create`

- Hozzon létre egy pull requestet, meghatározva a címet és a leírást az aktuális ág commit üzeneteiből:

`gh pr create --fill`

- Hozzon létre egy pull request tervezetet:

`gh pr create --draft`

- Pull request létrehozása az alapág, a cím és a leírás megadásával:

`gh pr create --base {{base_branch}} --title "{{title}}" --body "{{body}}"`

- Pull-kérelem megnyitásának megkezdése az alapértelmezett webböngészőben:

`gh pr create --web`
