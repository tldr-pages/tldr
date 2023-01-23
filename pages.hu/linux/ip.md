# ip

> Útválasztás, eszközök, házirend szerinti útválasztás és alagutak megjelenítése/manipulálása. Néhány alparancsnak, mint például a `ip address`, saját használati dokumentációja van. További információ: <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- Interfészek listázása részletes információkkal:

`ip address`

- Interfészek listázása rövid hálózati rétegbeli információkkal:

`ip -brief address`

- Interfészek listázása rövid linkréteg-információkkal:

`ip -brief link`

- Az útválasztási táblázat megjelenítése:

`ip route`

- Szomszédok megjelenítése (ARP-tábla):

`ip neighbour`

- Egy interfész fel/leállítása:

`ip link set {{interface}} up/down`

- IP-cím hozzáadása/törlése egy interfészhez:

`ip addr add/del {{ip}}/{{mask}} dev {{interface}}`

- Alapértelmezett útvonal hozzáadása:

`ip route add default via {{ip}} dev {{interface}}`
