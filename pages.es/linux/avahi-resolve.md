# avahi-resolve

> Traduce entre nombres de host y direcciones IP.
> Más información: <https://manned.org/avahi-resolve>.

- Resuelve un servicio local a su dirección IPv4:

`avahi-resolve -4 {{[-n|--name]}} {{servicio.local}}`

- Resuelve una dirección IP a un nombre de host, de manera detallada:

`avahi-resolve {{[-v|--verbose]}} {{[-a|--address]}} {{IP}}`
