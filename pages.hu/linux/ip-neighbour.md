# ip neighbour

> Szomszéd/ARP-táblák kezelése IP-alparancs. További információ: <https://manned.org/ip-neighbour.8>.

- A szomszédos/ARP-táblák bejegyzéseinek megjelenítése:

`ip neighbour`

- A `eth0` eszközön lévő szomszédtábla bejegyzéseinek eltávolítása:

`sudo ip neighbour flush dev {{eth0}}`

- Szomszédkeresés végrehajtása és szomszédos bejegyzés visszaadása:

`ip neighbour get {{lookup_ip}} dev {{eth0}}`

- ARP-bejegyzés hozzáadása vagy törlése a szomszédos IP-címhez a `eth0`:

`sudo ip neighbour {{add|del}} {{ip_address}} lladdr {{mac_address}} dev {{eth0}} nud reachable`

- A szomszédos IP-címhez tartozó ARP-bejegyzés módosítása vagy cseréje a `eth0`:

`sudo ip neighbour {{change|replace}} {{ip_address}} lladdr {{new_mac_address}} dev {{eth0}}`
