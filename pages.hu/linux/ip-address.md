# ip address

> IP-címkezelés alparancs. További információ: <https://manned.org/ip-address>.

- Hálózati interfészek és a hozzájuk tartozó IP-címek listázása:

`ip address`

- Szűrés, hogy csak az aktív hálózati interfészek jelenjenek meg:

`ip address show up`

- Egy adott hálózati interfészre vonatkozó információk megjelenítése:

`ip address show dev {{eth0}}`

- IP-cím hozzáadása egy hálózati interfészhez:

`ip address add {{ip_address}} dev {{eth0}}`

- IP-cím eltávolítása egy hálózati interfészről:

`ip address delete {{ip_address}} dev {{eth0}}`

- Egy adott hatókörbe tartozó összes IP-cím törlése egy hálózati interfészről:

`ip address flush dev {{eth0}} scope {{global|host|link}}`
