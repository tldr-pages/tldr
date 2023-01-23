# git filter-repo

> Sokoldalú eszköz a Git előzmények átírására. Lásd még: `bfg`. További információ: <https://github.com/newren/git-filter-repo>.

- Egy érzékeny karakterlánc cseréje az összes fájlban:

`git filter-repo --replace-text <(echo '{{find}}==>{{replacement}}')`

- Egyetlen mappa kivonása, az előzmények megtartásával:

`git-filter-repo --path {{path/to/folder}}`

- Egyetlen mappa eltávolítása, az előzmények megtartásával:

`git-filter-repo --path {{path/to/folder}} --invert-paths`

- Mindent áthelyez egy almappából egy szinttel feljebb:

`git-filter-repo --path-rename {{path/to/folder/:}}`
