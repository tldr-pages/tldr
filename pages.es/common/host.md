# host

> Busca registros de nombres de dominio.
> Vea también: `dig`, `resolvectl`, `nslookup`.
> Más información: <https://manned.org/host>.

- Busca registros A, AAAA y MX de un dominio:

`host {{dominio}}`

- Busca un campo (CNAME, TXT, ...) de un dominio:

`host -t {{campo}} {{dominio}}`

- Busca una IP inversa:

`host {{dirección_ip}}`

- Especifica un servidor DNS alternativo para consultar:

`host {{dominio}} {{8.8.8.8}}`
