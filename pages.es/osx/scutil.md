# scutil

> Gestiona los parámetros de configuración del sistema.
> Es necesario ser root para establecer la configuración.
> Más información: <https://ss64.com/osx/scutil.html>.

- Muestra la configuración DNS:

`scutil --dns`

- Muestra la configuración del proxy:

`scutil --proxy`

- Obtén el nombre del equipo:

`scutil --get ComputerName`

- Establece el nombre del equipo:

`sudo scutil --set ComputerName {{nombre_ordenador}}`

- Obtén el nombre del host:

`scutil --get HostName`

- Establece nombre del host:

`scutil --set HostName {{nombre_host}}`
