# service

> Gestionați serviciile executând scripturi de inițializare.
> Calea completă a scriptului trebuie omisă (`/etc/init.d/` se presupune).

- Listați numele și starea tuturor serviciilor:

`service --status-all`

- Serviciul Start/Stop/Repornire/Reîncărcare (start/stop ar trebui să fie întotdeauna disponibil):

`service {{service_name}} {{start|stop|restart|reload}}`

- Reporniți complet (rulează script de două ori cu start și stop):

`service {{service_name}} --full-restart`

- Afișați starea curentă a unui serviciu:

`service {{service_name}} status`
