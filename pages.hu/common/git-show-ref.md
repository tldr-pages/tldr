# git show-ref

> Git parancs a hivatkozások listázására. További információ: <https://git-scm.com/docs/git-show-ref>.

- Az összes hivatkozás megjelenítése az adattárban:

`git show-ref`

- Csak a fejekre vonatkozó hivatkozások megjelenítése:

`git show-ref --heads`

- Csak címkehivatkozások megjelenítése:

`git show-ref --tags`

- Ellenőrizze, hogy egy adott hivatkozás létezik-e:

`git show-ref --verify {{path/to/ref}}`
