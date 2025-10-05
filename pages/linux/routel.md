# routel

> List IP routing in a human readable format.
> See also: `ip route`, `route`.
> More information: <https://manned.org/man/routel>.

- Display the default routing table:

`routel`

- Display a specific routing table:

`routel {{table_number|main|local|default}}`

- Display only IPv4 routes:

`routel {{[-4|--family inet]}}`

- Display only IPv6 routes:

`routel {{[-6|--family inet6]}}`
