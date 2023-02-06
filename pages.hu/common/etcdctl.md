# etcdctl

> CLI-interfész az etcd-vel, egy nagy rendelkezésre állású kulcs-érték páros tárolóval való interakcióhoz. További információ: <https://etcd.io/docs/latest/dev-guide/interacting_v3/>.

- Megjeleníti a megadott kulcshoz tartozó értéket:

`etcdctl get {{my/key}}`

- Kulcs-érték pár tárolása:

`etcdctl put {{my/key}} {{my_value}}`

- Kulcs-érték pár törlése:

`etcdctl del {{my/key}}`

- Kulcs-érték pár tárolása, az érték beolvasása egy fájlból:

`etcdctl put {{my/file}} < {{path/to/file.txt}}`

- Az etcd kulcstároló pillanatfelvételének mentése:

`etcdctl snapshot save {{path/to/snapshot.db}}`

- Az etcd keystore pillanatfelvételének visszaállítása (az etcd-kiszolgáló újraindítása után):

`etcdctl snapshot restore {{path/to/snapshot.db}}`

- Felhasználó hozzáadása:

`etcdctl user add {{my_user}}`

- Egy kulcs változásainak figyelése:

`etcdctl watch {{my/key}}`
