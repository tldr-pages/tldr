# git reflog

> A helyi hivatkozások, például a HEAD, az ágak vagy a címkék változásainak naplózása. További információ: <https://git-scm.com/docs/git-reflog>.

- Megjeleníti a HEAD-reflogot:

`git reflog`

- Egy adott ág reflogjának megjelenítése:

`git reflog {{branch_name}}`

- Csak a reflog 5 legfrissebb bejegyzésének megjelenítése:

`git reflog -n {{5}}`
