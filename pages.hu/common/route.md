# route

> Az útvonalterv beállításához használja a route cmd-t. További információ: <https://manned.org/route>.

- Az útvonaltábla információinak megjelenítése:

`route -n`

- Útvonalszabály hozzáadása:

`sudo route add -net {{ip_address}} netmask {{netmask_address}} gw {{gw_address}}`

- Útvonalszabály törlése:

`sudo route del -net {{ip_address}} netmask {{netmask_address}} dev {{gw_address}}`
