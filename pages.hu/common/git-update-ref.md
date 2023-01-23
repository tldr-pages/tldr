# git update-ref

> Git parancs a Git-referenciák létrehozására, frissítésére és törlésére. További információ: <https://git-scm.com/docs/git-update-ref>.

- Ref törlése, hasznos az első commit puha visszaállításához:

`git update-ref -d {{HEAD}}`

- Ref frissítése üzenettel:

`git update-ref -m {{message}} {{HEAD}} {{4e95e05}}`
