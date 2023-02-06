# git switch

> Váltás a Git ágak között. A Git 2.23+ verziója szükséges. Lásd még: `git checkout`. További információ: <https://git-scm.com/docs/git-switch>.

- Váltás egy meglévő ágra:

`git switch {{branch_name}}`

- Hozzon létre egy új ágat, és váltson rá:

`git switch --create {{branch_name}}`

- Új ág létrehozása egy meglévő commit alapján és váltás rá:

`git switch --create {{branch_name}} {{commit}}`

- Váltás az előző ágra:

`git switch -`

- Egy ágra váltás és az összes almodul frissítése:

`git switch --recurse-submodules {{branch_name}}`

- Egy ágra váltás és az aktuális ág és a még el nem könyvelt módosítások automatikus egyesítése:

`git switch --merge {{branch_name}}`
