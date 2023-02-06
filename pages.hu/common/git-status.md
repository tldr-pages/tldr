# git status

> Megjeleníti a Git-repositoryban lévő fájlok változásait. A megváltozott, hozzáadott és törölt fájlokat listázza az aktuálisan kiadott commithoz képest. További információ: <https://git-scm.com/docs/git-status>.

- Megjeleníti azokat a megváltozott fájlokat, amelyek még nincsenek hozzáadva a commithoz:

`git status`

- Kimenetet ad \[s\]hort formátumban:

`git status -s`

- Ne jelenítse meg a kimeneten a még nem követett fájlokat:

`git status --untracked-files=no`

- Kimenet megjelenítése \[s\]hort formátumban a \[b\]ranch infóval együtt:

`git status -sb`
