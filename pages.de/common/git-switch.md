# git switch

> Wechsle zwischen Branches. Verfügbar ab Git Version 2.23+.
> Siehe auch `git checkout`.
> Weitere Informationen: <https://git-scm.com/docs/git-switch>.

- Wechsle zu einem existierenden Branch:

`git switch {{branche_name}}`

- Erstelle einen neuen Branch und wechsele zu diesem:

`git switch {{[-c|--create]}} {{branch_name}}`

- Erstelle einen neuen Branch basierend auf einem existierenden Commit und wechsele zu diesem:

`git switch {{[-c|--create]}} {{branch_name}} {{commit}}`

- Wechsele zum vorherigen Branch:

`git switch -`

- Wechsele zu einem Branch und aktualisiere alle Submodule entsprechend:

`git switch --recurse-submodules {{branch_name}}`

- Wechsele zu einem Branch und merge automatisch den aktuellen Branch und alle Änderungen, die nicht committed wurden:

`git switch {{[-m|--merge]}} {{branch_name}}`
