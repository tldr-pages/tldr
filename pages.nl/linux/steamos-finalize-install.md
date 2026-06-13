# steamos-finalize-install

> Voltooi de installatie van SteamOS door bootloaders in te stellen en systeemupdates toe te passen.
> Meer informatie: <https://gitlab.com/users/evlaV/projects>.

- Voltooi de installatie:

`sudo steamos-finalize-install`

- Voltooi zonder bootloaders of kernel bij te werken:

`sudo steamos-finalize-install --no-bootloaders --no-kernel`

- Sla alle migratiestappen over:

`sudo steamos-finalize-install --no-migrate`

- Stel een specifieke root-hash in tijdens het voltooien:

`sudo steamos-finalize-install --roothash {{hash}}`

- Forceer systeem-migratiestappen ongeacht de omgeving:

`sudo steamos-finalize-install --force`
