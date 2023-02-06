# git describe

> Adjon egy objektumnak egy ember által olvasható nevet egy rendelkezésre álló hivatkozás alapján. További információ: <https://git-scm.com/docs/git-describe>.

- Egyedi nevet hoz létre az aktuális commithoz (a név tartalmazza a legutóbbi megjegyzett taget, a további commitok számát és a rövidített commit hash-t):

`git describe`

- Hozzon létre egy 4 számjegyű nevet a rövidített commit hash számára:

`git describe --abbrev={{4}}`

- Létrehoz egy nevet a címkehivatkozás elérési útvonalával:

`git describe --all`

- Egy Git-tag leírása:

`git describe {{v1.0.0}}`

- Egy adott ág utolsó commitjának nevének létrehozása:

`git describe {{branch_name}}`
