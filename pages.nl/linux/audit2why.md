# audit2why

> Leg SELinux-weigeringen van auditlogs uit.
> Onderdeel van het `policycoreutils-python-utils` pakket.
> Zie ook: `audit2allow`, `ausearch`, `sealert`.
> Meer informatie: <https://manned.org/audit2why>.

- Leg de nieuwste SELinux-weigering uit:

`sudo audit2why`

- Leg SELinux-weigeringen van een specifiek auditlogbestand uit:

`sudo audit2why {{[-i|--input]}} {{pad/naar/audit.log}}`

- Leg alle SELinux-weigeringen van een auditlog uit:

`sudo ausearch {{[-m|--message]}} avc | audit2why`

- Leg weigeringen van een specifieke service uit:

`sudo ausearch {{[-m|--message]}} avc {{[-c|--comm]}} {{service_naam}} | audit2why`
