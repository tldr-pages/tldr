# git worktree

> Több, ugyanahhoz az adattárhoz kapcsolódó munkafa kezelése. További információ: <https://git-scm.com/docs/git-worktree>.

- Új könyvtár létrehozása a megadott ággal, amelybe a megadott ágat kipipálja:

`git worktree add {{path/to/directory}} {{branch}}`

- Új könyvtár létrehozása egy új ággal, amelybe egy új ágat ellenőrzött ki:

`git worktree add {{path/to/directory}} -b {{new_branch}}`

- Az összes, ehhez az adattárhoz csatolt munkakönyvtár listázása:

`git worktree list`

- Egy munkafa eltávolítása (munkafa könyvtár törlése után):

`git worktree prune`
