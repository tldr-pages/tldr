# git show-branch

> Az ágak és commitjaik megjelenítése. További információ: <https://git-scm.com/docs/git-show-branch>.

- Egy ág legutóbbi commitjának összefoglalója:

`git show-branch {{branch_name|ref|commit}}`

- Több commit vagy ág történetének commitjainak összehasonlítása:

`git show-branch {{branch_name|ref|commit}}`

- Az összes távoli követési ág összehasonlítása:

`git show-branch --remotes`

- Mind a helyi, mind a távoli követési ágak összehasonlítása:

`git show-branch --all`

- Az összes ág legutóbbi commitjainak listázása:

`git show-branch --all --list`

- Egy adott ág összehasonlítása az aktuális ággal:

`git show-branch --current {{commit|branch_name|ref}}`

- A commit nevének megjelenítése a relatív név helyett:

`git show-branch --sha1-name --current {{current|branch_name|ref}}`

- A közös ős után adott számú commitot továbblépni:

`git show-branch --more {{5}} {{commit|branch_name|ref}} {{commit|branch_name|ref}} {{...}}`
