# syncthing

> Folyamatos kétirányú decentralizált mappaszinkronizáló eszköz. További információ: <https://docs.syncthing.net/>.

- Indítsa el a Syncthinget:

`syncthing`

- A Syncthing elindítása webböngésző megnyitása nélkül:

`syncthing -no-browser`

- Nyomtassa ki az eszköz azonosítóját:

`syncthing -device-id`

- A kezdeti könyvtár megváltoztatása:

`syncthing -home={{path/to/directory}}`

- Teljes indexcsere kikényszerítése:

`syncthing -reset-deltas`

- A cím módosítása, amelyen a webes felület hallgat:

`syncthing -gui-address={{ip_address:port|path/to/socket.sock}}`

- A Syncthing által használt fájlok elérési útvonalának megjelenítése:

`syncthing -paths`

- A Syncthing monitorfolyamat letiltása:

`syncthing -no-restart`
