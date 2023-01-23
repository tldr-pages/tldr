# ip route

> IP Routing table management alparancs. További információ: <https://manned.org/ip-route>.

- Az útválasztási táblázat megjelenítése:

`ip route {{show|list}}`

- Alapértelmezett útvonal hozzáadása átjáró-továbbítással:

`sudo ip route add default via {{gateway_ip}}`

- Alapértelmezett útvonal hozzáadása a `eth0` segítségével:

`sudo ip route add default dev {{eth0}}`

- Statikus útvonal hozzáadása:

`sudo ip route add {{destination_ip}} via {{gateway_ip}} dev {{eth0}}`

- Statikus útvonal törlése:

`sudo ip route del {{destination_ip}} dev {{eth0}}`

- Statikus útvonal módosítása vagy cseréje:

`sudo ip route {{change|replace}} {{destination_ip}} via {{gateway_ip}} dev {{eth0}}`

- Megmutatja, hogy a kernel melyik útvonalat használja egy IP-cím eléréséhez:

`ip route get {{destination_ip}}`
