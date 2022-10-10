# svcadm

> Manipuleer service instanties.
> Meer informatie: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Inschakelen van een service in de service database:

`svcadm enable {{service_name}}`

- Uitschakelen van een service in de service database:

`svcadm disable {{service_name}}`

- Herstarten van een draaiende service:

`svcadm restart {{service_name}}`

- refresh de configuratie van een service:

`svcadm refresh {{service_name}}`

- Haal een service uit maintenance state, en schakel deze in:

`svcadm clear {{service_name}}`
