# legit

> Kiegészítő parancssori felület a Git-hez. További információ: <https://frostming.github.io/legit>.

- Átváltás egy megadott ágra, a nem tárolt változtatások elrejtése és visszaállítása:

`git switch {{target_branch}}`

- Az aktuális ág szinkronizálása, automatikus összevonás vagy újraszinkronizálás, valamint a stashing és unstashing:

`git sync`

- Megadott ág közzététele a távoli kiszolgálón:

`git publish {{branch_name}}`

- Egy ág eltávolítása a távoli kiszolgálóról:

`git unpublish {{branch_name}}`

- Az összes ág listázása és közzétételük állapota:

`git branches {{glob_pattern}}`

- Az utolsó commit eltávolítása az előzményekből:

`git undo {{--hard}}`
