# rc-service

> Găsiți și executați serviciile OpenRC cu argumente.
> A se vedea, de asemenea, `openrc`.

- Arată starea unui serviciu:

`rc-service {{service_name}} status`

- Începe un serviciu:

`sudo rc-service {{service_name}} start`

- Opreşte un serviciu:

`sudo rc-servie {{service_name}} stop`

- Reporniți un serviciu:

`sudo rc-service {{service_name}} restart`

- Simulați rularea comenzii personalizate a unui serviciu:

`sudo rc-service --dry-run {{service_name}} {{command_name}}`

- De fapt, rulați comanda personalizată a unui serviciu:

`sudo rc-service {{service_name}} {{command_name}}`

- Rezolvarea locației unei definiții de serviciu pe disc:

`sudo rc-service --resolve {{service_name}}`
