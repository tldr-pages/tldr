# git revert

> Új commitok létrehozása, amelyek visszafordítják a korábbiak hatását. További információ: <https://git-scm.com/docs/git-revert>.

- A legutóbbi commit visszavonása:

`git revert {{HEAD}}`

- Az 5. utolsó commit visszavonása:

`git revert HEAD~{{4}}`

- Több commit visszavonása:

`git revert {{branch_name~5..branch_name~2}}`

- Ne hozzon létre új commitokat, csak a munkafát változtassa meg:

`git revert -n {{0c01a9..9a1743}}`
