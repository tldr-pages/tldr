# git checkout

> A munkafa egy ágának vagy ösvényeinek ellenőrzése. További információ: <https://git-scm.com/docs/git-checkout>.

- Új ág létrehozása és váltás:

`git checkout -b {{branch_name}}`

- Új ág létrehozása és váltás egy új ágra egy adott hivatkozás alapján (az ág, a távoli ág/ág, a címke példák az érvényes hivatkozásokra):

`git checkout -b {{branch_name}} {{reference}}`

- Meglévő helyi ágra váltás:

`git checkout {{branch_name}}`

- Átváltás a korábban kipipált ágra:

`git checkout -`

- Váltás egy meglévő távoli ágra:

`git checkout --track {{remote_name}}/{{branch_name}}`

- Az aktuális könyvtárban lévő összes, még el nem végzett változtatás elvetése (további undo-szerű parancsokért lásd: `git reset` ):

`git checkout .`

- Egy adott fájl még el nem végzett módosításainak elvetése:

`git checkout {{path/to/file}}`

- Az aktuális könyvtárban lévő fájl cseréje az adott ágban lekötött verzióra:

`git checkout {{branch_name}} -- {{path/to/file}}`
