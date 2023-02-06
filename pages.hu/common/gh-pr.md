# gh pr

> A GitHub pull requestek kezelése a parancssorból. Néhány alparancsnak, mint például a `gh pr create`, saját használati dokumentációja van. További információ: <https://cli.github.com/manual/gh_pr>.

- Hozzon létre egy pull requestet:

`gh pr create`

- Egy adott pull request helyi ellenőrzése:

`gh pr checkout {{pr_number}}`

- A pull requestben az aktuális ágban végrehajtott változtatások megtekintése:

`gh pr diff`

- A pull request jóváhagyása az aktuális ághoz:

`gh pr review --approve`

- Az aktuális ághoz tartozó pull request egyesítése interaktívan:

`gh pr merge`

- A pull request interaktív szerkesztése:

`gh pr edit`

- A pull request alapágának szerkesztése:

`gh pr edit --base {{branch_name}}`

- Az aktuális adattár pull-kérelmeinek állapotának ellenőrzése:

`gh pr status`
