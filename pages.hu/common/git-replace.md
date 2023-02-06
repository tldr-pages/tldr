# git replace

> Az objektumok helyettesítésére szolgáló hivatkozások létrehozása, listázása és törlése. További információ: <https://git-scm.com/docs/git-replace>.

- Bármely commit cseréje egy másikra, a többi commit változatlanul hagyása mellett:

`git replace {{object}} {{replacement}}`

- A megadott objektumok meglévő helyettesítő hivatkozásainak törlése:

`git replace --delete {{object}}`

- Egy objektum tartalmának interaktív szerkesztése:

`git replace --edit {{object}}`
