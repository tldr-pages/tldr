# git feature

> Feature-ágak létrehozása vagy egyesítése. A feature-ágak a feature/ formátumnak felelnek meg. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-feature>.

- Új funkcióág létrehozása és átváltása:

`git feature {{feature_branch}}`

- Egy feature-ág beolvasztása az aktuális ágba egy beolvasztási commit létrehozásával:

`git feature finish {{feature_branch}}`

- Egy feature-ág beolvasztása az aktuális ágba, a változtatások egy commitba való összevonása:

`git feature finish --squash {{feature_branch}}`

- Egy adott feature branch változásainak elküldése a távoli megfelelőjének:

`git feature {{feature_branch}} --remote {{remote_name}}`
