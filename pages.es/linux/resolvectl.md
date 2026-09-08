# resolvectl

> Resuelve nombres de dominio, direcciones IPv4 e IPv6, registros de recursos DNS y servicios.
> Nota: `systemd-resolved.service` debe estar en ejecución.
> Vea también: `dig`, `nslookup`, `host`.
> Más información: <https://www.freedesktop.org/software/systemd/man/latest/resolvectl.html>.

- Muestra la configuración de DNS:

`resolvectl`

- Resuelve las direcciones IPv4 e IPv6 de uno o más dominios:

`resolvectl query {{dominio1 dominio2 ...}}`

- Obtiene el dominio de una dirección IP especificada:

`resolvectl query {{dirección_IP}}`

- Vacía todas las cachés DNS locales:

`resolvectl flush-caches`

- Muestra estadísticas de DNS (transacciones, caché y veredictos DNSSEC):

`resolvectl statistics`

- Obtiene un registro MX de un dominio:

`resolvectl --legend {{no}} {{[-t|--type]}} MX query {{dominio}}`

- Resuelve un registro SRV, por ejemplo `_xmpp-server._tcp gmail.com`:

`resolvectl service _{{servicio}}._{{protocolo}} {{nombre}}`

- Obtiene una clave TLS:

`resolvectl tlsa tcp {{dominio}}:443`
