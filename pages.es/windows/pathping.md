# pathping

> Una herramienta de traza de ruta que combina características de `ping` y `tracert`.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/pathping>.

- Realiza un ping y traza la ruta a un host:

`pathping {{nombre_del_host}}`

- No realiza la búsqueda inversa de la dirección IP al nombre de host:

`pathping {{nombre_del_host}} -n`

- Especifica el número máximo de saltos para buscar el objetivo (el valor predeterminado es 30):

`pathping {{nombre_del_host}} -h {{max_hops}}`

- Especifica los milisegundos a esperar entre pings (el valor predeterminado es 240):

`pathping {{nombre_del_host}} -p {{tiempo}}`

- Especifica el número de consultas por salto (el valor predeterminado es 100):

`pathping {{nombre_del_host}} -q {{consultas}}`

- Obliga al uso de IPV4:

`pathping {{nombre_del_host}} -4`

- Obliga al uso de IPV6:

`pathping {{nombre_del_host}} -6`

- Muestra la ayuda:

`pathping /?`
