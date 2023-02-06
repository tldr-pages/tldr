# rpcinfo

> RPC-hívást indít egy RPC-kiszolgáló felé, és jelenti, hogy mit talál. További információ: <https://manned.org/rpcinfo>.

- A localhost-on regisztrált összes RPC-szolgáltatás teljes táblázatának megjelenítése:

`rpcinfo`

- A localhost-on regisztrált összes RPC-szolgáltatás tömör táblázatának megjelenítése:

`rpcinfo -s {{localhost}}`

- A localhoston végzett rpcbind műveletek statisztikáinak táblázata:

`rpcinfo -m`

- Adott szolgáltatásnév (mountd) és verziószám (2) bejegyzései listájának megjelenítése egy távoli nfs megosztáson:

`rpcinfo -l {{remote_nfs_server_ip}} {{mountd}} {{2}}`

- A mountd szolgáltatás 1. verziójának regisztrációjának törlése az összes szállításhoz:

`rpcinfo -d {{mountd}} {{1}}`
