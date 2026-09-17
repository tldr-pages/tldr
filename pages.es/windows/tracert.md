# tracert

> Recibe información sobre cada paso en la ruta entre tu PC y el destino.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>.

- Rastrear una ruta:

`tracert {{ip}}`

- Evitar que `tracert` resuelva direcciones IP a nombres de host:

`tracert /d {{ip}}`

- Forzar que `tracert` use solo IPv4:

`tracert /4 {{ip}}`

- Forzar que `tracert` use solo IPv6:

`tracert /6 {{ip}}`

- Especificar el número máximo de saltos en la búsqueda del destino:

`tracert /h {{max_saltos}} {{ip}}`

- Mostrar ayuda:

`tracert /?`
