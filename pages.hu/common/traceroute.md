# traceroute

> Az útvonalcsomagok nyomon követése a hálózati állomáshoz. További információ: <https://manned.org/traceroute>.

- Traceroute egy állomáshoz:

`traceroute {{host}}`

- Az IP-cím és az állomásnév leképezésének letiltása:

`traceroute -n {{host}}`

- A válaszra való várakozási idő megadása:

`traceroute -w {{0.5}} {{host}}`

- A lekérdezések számának megadása ugrásonként:

`traceroute -q {{5}} {{host}}`

- A keresőcsomag méretének megadása bájtban:

`traceroute {{host}} {{42}}`
