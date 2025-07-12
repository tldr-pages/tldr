# pathping

> Una herramienta de traza de ruta que combina características de `ping` y `tracert`.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/pathping>.

- Hacer ping y trazar la ruta a un host:

`pathping {{nombre_del_host}}`

- No realizar la búsqueda inversa de la dirección IP al nombre de host:

`pathping {{nombre_del_host}} -n`

- Especificar el número máximo de saltos para buscar el objetivo (el valor predeterminado es 30):

`pathping {{nombre_del_host}} -h {{max_hops}}`

- Especificar los milisegundos a esperar entre pings (el valor predeterminado es 240):

`pathping {{nombre_del_host}} -p {{tiempo}}`

- Especificar el número de consultas por salto (el valor predeterminado es 100):

`pathping {{nombre_del_host}} -q {{consultas}}`

- Forzar el uso de IPV4:

`pathping {{nombre_del_host}} -4`

- Forzar el uso de IPV6:

`pathping {{nombre_del_host}} -6`

- Mostrar ayuda:

`pathping /?`
