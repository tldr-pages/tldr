# duplicacy

> Zármentes deduplikációs felhőmentő eszköz. További információ: <https://github.com/gilbertchen/duplicacy/wiki>.

- Az aktuális könyvtárat használja tárolóként, inicializál egy SFTP tárolót, és jelszóval titkosítja a tárolót:

`duplicacy init -e {{snapshot_id}} {{sftp://user@192.168.2.100/path/to/storage/}}`

- Mentse az adattár pillanatfelvételét az alapértelmezett tárolóba:

`duplicacy backup`

- Az aktuális adattár pillanatfelvételeinek listázása:

`duplicacy list`

- Az adattár visszaállítása egy korábban elmentett pillanatfelvételre:

`duplicacy restore -r {{revision}}`

- A pillanatfelvételek integritásának ellenőrzése:

`duplicacy check`

- Egy másik tároló hozzáadása a meglévő adattárhoz:

`duplicacy add {{storage_name}} {{snapshot_id}} {{storage_url}}`

- A pillanatfelvétel egy adott revíziójának metszése:

`duplicacy prune -r {{revision}}`

- Revíziók metszése, minden `n` naponként egy revízió megtartása a `m` napnál régebbi revíziók esetében:

`duplicacy prune -keep {{n:m}}`
