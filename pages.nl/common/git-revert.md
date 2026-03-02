# git revert

> Maak nieuwe commits aan die eerdere commits ongedaan maken.
> Meer informatie: <https://git-scm.com/docs/git-revert>.

- Maak de laatste commit ongedaan:

`git revert HEAD`

- Maak de vijfde laatste commit ongedaan:

`git revert HEAD~4`

- Maak een specifieke commit ongedaan:

`git revert {{0c01a9}}`

- Maak meerdere commits ongedaan:

`git revert {{branch_naam~5}}..{{branch_naam~2}}`

- Maak geen nieuwe commits aan, pas alleen de working tree aan:

`git revert {{[-n|--no-commit]}} {{0c01a9}}..{{9a1743}}`

- Annuleer een Git revert na een merge conflict:

`git revert --abort`
