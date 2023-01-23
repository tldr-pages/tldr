# ip route show

> Az IP-útválasztási tábla kezelésének megjelenítése alparancs. További információ: <https://manned.org/ip-route>.

- Az útválasztási táblázat megjelenítése:

`ip route show`

- A fő útválasztási táblázat megjelenítése (ugyanaz, mint az első példában):

`ip route show {{main|254}}`

- A helyi útválasztási táblázat megjelenítése:

`ip route show table {{local|255}}`

- Az összes útválasztási tábla megjelenítése:

`ip route show table {{all|unspec|0}}`

- Csak az adott eszközről származó útvonalak listázása:

`ip route show dev {{eth0}}`

- Egy adott hatókörön belüli útvonalak listázása:

`ip route show scope link`

- Az útválasztási gyorsítótár megjelenítése:

`ip route show cache`

- Csak IPv6 vagy IPv4 útvonalak megjelenítése:

`ip {{-6|-4}} route show`
