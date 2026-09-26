# tracert

> Recibe información sobre cada paso en la ruta entre tu PC y el destino.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>.

- Rastrea una ruta:

`tracert {{ip}}`

- Evita que `tracert` resuelva direcciones IP a nombres de host:

`tracert /d {{ip}}`

- Obliga a que `tracert` use solo IPv4:

`tracert /4 {{ip}}`

- Obliga a que `tracert` use solo IPv6:

`tracert /6 {{ip}}`

- Especifica el número máximo de saltos en la búsqueda del destino:

`tracert /h {{max_saltos}} {{ip}}`

- Muestra la ayuda:

`tracert /?`
