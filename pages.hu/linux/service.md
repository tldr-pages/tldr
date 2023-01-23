# service

> A szolgáltatások kezelése init szkriptek futtatásával. A teljes szkript elérési útvonalát el kell hagyni (`/etc/init.d/` feltételezhető). További információ: <https://manned.org/service>.

- Az összes szolgáltatás nevének és állapotának listázása:

`service --status-all`

- Start/Stop/Restart/Restart/Reload service (a start/stop szolgáltatásnak mindig elérhetőnek kell lennie):

`service {{service_name}} {{start|stop|restart|reload}}`

- Teljes újraindítás (a szkript kétszer fut le a start és a stop funkcióval):

`service {{service_name}} --full-restart`

- Megmutatja a szolgáltatás aktuális állapotát:

`service {{service_name}} status`
