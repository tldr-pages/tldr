# loginctl

> A systemd bejelentkezési menedzser kezelése. További információ: <https://www.freedesktop.org/software/systemd/man/loginctl.html>.

- Az összes aktuális munkamenet kinyomtatása:

`loginctl list-sessions`

- Egy adott munkamenet összes tulajdonságának kinyomtatása:

`loginctl show-session {{session_id}} --all`

- Egy adott felhasználó összes tulajdonságának nyomtatása:

`loginctl show-user {{username}}`

- Egy felhasználó egy adott tulajdonságának nyomtatása:

`loginctl show-user {{username}} --property={{property_name}}`

- A `loginctl` művelet végrehajtása egy távoli állomáson:

`loginctl list-users -H {{hostname}}`
