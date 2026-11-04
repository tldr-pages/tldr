# tracert

> Recibe información sobre cada paso en la ruta entre tu PC y el destino.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>.

- Rastrea una ruta:

`tracert {{ip_address}}`

- Evita que `tracert` resuelva direcciones IP a nombres de host:

`tracert /d {{ip_address}}`

- Obliga a que `tracert` use solo IPv4:

`tracert /4 {{ip_address}}`

- Obliga a que `tracert` use solo IPv6:

`tracert /6 {{ip_address}}`

- Especifica el número máximo de saltos en la búsqueda del destino:

`tracert /h {{max_saltos}} {{ip_address}}`

- Muestra la ayuda:

`tracert /?`
