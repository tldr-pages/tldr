# gh pr merge

> GitHub pull requestek egyesítése. További információ: <https://cli.github.com/manual/gh_pr_merge>.

- Az aktuális ághoz tartozó pull request egyesítése interaktívan:

`gh pr merge`

- A megadott pull request egyesítése interaktívan:

`gh pr merge {{pr_number}}`

- A pull request egyesítése, az ág eltávolítása a helyi és a távoli ágon egyaránt:

`gh pr merge --delete-branch`

- Az aktuális pull request egyesítése a megadott egyesítési stratégiával:

`gh pr merge --{{merge|squash|rebase}}`

- Az aktuális pull request egyesítése a megadott egyesítési stratégiával és commit üzenettel:

`gh pr merge --{{merge|squash|rebase}} --subject {{commit_message}}`

- Az aktuális pull request összezsúfolása egy commitba az üzenettesttel és az egyesítéssel:

`gh pr merge --squash --body="{{commit_message_body}}"`

- Súgó megjelenítése:

`gh pr merge --help`
