# debchange

> Mantiene el archivo debian/log de cambios (changelog) de un paquete fuente de Debian.
> Más información: <https://manned.org/debchange.1>.

- Agrega una nueva versión para una subida que no es del mantenedor al registro (log) de cambios:

`debchange --nmu`

- Agrega una entrada de cambio a la versión actual:

`debchange --append`

- Agrega una entrada de cambio para cerrar el fallo con un ID específico:

`debchange --closes {{id_del_fallo}}`
