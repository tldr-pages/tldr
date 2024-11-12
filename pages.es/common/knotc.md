# knotc

> Controla el servidor DNS knot.
> Más información: <https://www.knot-dns.cz/docs/latest/html/man_knotc.html>.

- Comienza a editar una zona:

`knotc zone-begin {{zona}}`

- Establece un registro A con TTL de 3600:

`knotc zone-set {{zona}} {{subdominio}} 3600 A {{dirección_ip}}`

- Finaliza la edición de la zona:

`knotc zone-commit {{zona}}`

- Obtén los datos de la zona actual:

`knotc zone-read {{zona}}`

- Obtén la configuración actual del servidor:

`knotc conf-read server`
