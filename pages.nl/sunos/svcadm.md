# svcadm

> Manipuleer serviceinstanties.
> Meer informatie: <https://www.unix.com/man-page/sunos/1m/svcadm>.

- Schakel een service in de servicedatabase in:

`svcadm enable {{service_naam}}`

- Schakel een service in de servicedatabase uit:

`svcadm disable {{service_naam}}`

- Herstart een draaiende service:

`svcadm restart {{service_naam}}`

- Herlaad de configuratie van een service:

`svcadm refresh {{service_naam}}`

- Haal een service uit maintenance state, en schakel deze in:

`svcadm clear {{service_naam}}`
