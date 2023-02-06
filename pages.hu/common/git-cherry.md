# git cherry

> Olyan commitok keresése, amelyeket még nem alkalmaztak upstream-en. További információ: <https://git-scm.com/docs/git-cherry>.

- Megjeleníti a commitokat (és üzeneteiket) az upstream egyenértékű commitokkal:

`git cherry -v`

- Adjon meg egy másik upstream és témaágat:

`git cherry {{origin}} {{topic}}`

- Korlátozza a commitokat egy adott határon belüliekre:

`git cherry {{origin}} {{topic}} {{base}}`
