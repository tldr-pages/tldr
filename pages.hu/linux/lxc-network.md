# lxc network

> Az LXD konténerek hálózatainak kezelése. További információ: <https://linuxcontainers.org/lxd/docs/master/networks>.

- Az összes elérhető hálózat listázása:

`lxc network list`

- Egy adott hálózat konfigurációjának megjelenítése:

`lxc network show {{network_name}}`

- Futtatott példány hozzáadása egy adott hálózathoz:

`lxc network attach {{network_name}} {{container_name}}`

- Új kezelt hálózat létrehozása:

`lxc network create {{network_name}}`

- Egy adott hálózat hídinterfészének beállítása:

`lxc network set {{network_name}} bridge.external_interfaces {{eth0}}`

- NAT letiltása egy adott hálózathoz:

`lxc network set {{network_name}} ipv{{4}}.nat false`
