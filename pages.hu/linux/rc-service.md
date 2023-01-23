# rc-service

> OpenRC szolgáltatások keresése és futtatása argumentumokkal. Lásd még: `openrc`. További információ: <https://manned.org/rc-service>.

- Egy szolgáltatás állapotának megjelenítése:

`rc-service {{service_name}} status`

- Egy szolgáltatás elindítása:

`sudo rc-service {{service_name}} start`

- Egy szolgáltatás leállítása:

`sudo rc-service {{service_name}} stop`

- Egy szolgáltatás újraindítása:

`sudo rc-service {{service_name}} restart`

- Egy szolgáltatás egyéni parancsának futtatásának szimulálása:

`sudo rc-service --dry-run {{service_name}} {{command_name}}`

- Egy szolgáltatás egyéni parancsának tényleges futtatása:

`sudo rc-service {{service_name}} {{command_name}}`

- A szolgáltatásdefiníció helyének meghatározása a lemezen:

`sudo rc-service --resolve {{service_name}}`
