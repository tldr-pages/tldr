# rpcinfo

> Maak een RPC-oproep naar een RPC-server en rapporteert wat het vindt.
> Meer informatie: <https://manned.org/rpcinfo>.

- Toon volledige tabel van alle RPC-diensten geregistreerd op localhost:

`rpcinfo`

- Toon beknopte tabel van alle RPC-diensten geregistreerd op localhost:

`rpcinfo -s {{localhost}}`

- Toon tabel met statistieken van rpcbind-operaties op localhost:

`rpcinfo -m`

- Toon lijst van items van een bepaalde service naam (mountd) en versienummer (2) op een remote nfs-share:

`rpcinfo -l {{remote_nfs_server_ip}} {{mountd}} {{2}}`

- Verwijder de registratie voor versie 1 van de mountd-service voor alle transporten:

`rpcinfo -d {{mountd}} {{1}}`
