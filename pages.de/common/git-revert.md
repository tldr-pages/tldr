# git revert

> Erstelle neue Commits, die die Wirkung früherer Commits umkehren.
> Weitere Informationen: <https://git-scm.com/docs/git-revert>.

- Mache den letzten Commit rückgängig:

`git revert {{HEAD}}`

- Mache den 5-vorletzten Commit rückgängig:

`git revert HEAD~{{4}}`

- Mache einen bestimmten Commit rückgängig:

`git revert {{0c01a9}}`

- Mache mehrere Commits rückgängig:

`git revert {{branch_name~5..branch_name~2}}`

- Erstelle keine neuen Commits, ändere nur das Arbeitsverzeichnis:

`git revert {{[-n|--no-commit]}} {{0c01a9..9a1743}}`

- Breche ein Git revert nach einem Merge-Konflikt ab:

`git revert --abort`
