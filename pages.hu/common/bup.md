# bup

> A Git packfile formátumon alapuló biztonsági mentési rendszer, amely inkrementális mentést és globális deduplikációt biztosít. További információ: <https://github.com/bup/bup>.

- Biztonsági mentési adattár inicializálása a megadott helyi könyvtárban:

`bup -d {{path/to/repository}} init`

- Egy adott könyvtár előkészítése a biztonsági mentés elkészítése előtt:

`bup -d {{path/to/repository}} index {{path/to/directory}}`

- Biztonsági mentés egy könyvtárról az adattárba:

`bup -d {{path/to/repository}} save -n {{backup_name}} {{path/to/directory}}`

- Az adattárban jelenleg tárolt biztonsági mentések pillanatfelvételeinek megjelenítése:

`bup -d {{path/to/repository}} ls`

- Egy adott biztonsági mentési pillanatkép visszaállítása egy célkönyvtárba:

`bup -d {{path/to/repository}} restore -C {{path/to/target_directory}} {{backup_name}}`
