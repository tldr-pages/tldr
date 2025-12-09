# route

> Gebruik het route-commando om de routetabel in te stellen.
> Meer informatie: <https://manned.org/route>.

- Toon de informatie van de routetabel:

`route -n`

- Voeg een routeregel toe:

`sudo route add -net {{ip_adres}} netmask {{netmask_adres}} gw {{gw_adres}}`

- Verwijder een routeregel:

`sudo route del -net {{ip_adres}} netmask {{netmask_adres}} dev {{gw_adres}}`
