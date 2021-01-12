# git switch

> Wechsle zwischen Branches. Verfügbar ab Git Version 2.23+.
> Betrachte auch `git checkout`.
> Mehr Informationen: <https://git-scm.com/docs/git-switch>.

- Wechsele zu einem existierenden Branch:

`git switch {{name_des_branches}}`

- Erstelle einen neuen Branch und wechsele zu diesem:

`git switch --create {{name_des_branches}}`

- Erstelle einen neuen Branch basierend auf einem existierenden Commit und wechsele zu diesem:

`git switch --create {{name_des_branches}} {{commit}}`

- Wechsele zu dem vorherigen Branch:

`git switch -`

- Wechsele zu einem Branch und aktualisiere alle Submodule entsprechend:

`git switch --recurse-submodules {{name_des_branches}}`

- Wechsele zu einem Branch und merge automatisch den aktuellen Branch und alle Änderungen, die nicht committed wurden:

`git switch --merge {{name_des_branches}}`
