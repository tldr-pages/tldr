# scutil

> Gestiona los parámetros de configuración del sistema.
> Es necesario ser root para establecer la configuración.
> Más información: <https://ss64.com/osx/scutil.html>.

- Muestra la configuración DNS:

`scutil --dns`

- Muestra la configuración del proxy:

`scutil --proxy`

- Obtiene nombre de equipo:

`scutil --get NombreOrdenador`

- Establece el nombre del equipo:

`sudo scutil --set NombreOrdenador {{nombre_ordenador}}`

- Obtiene nombre del host:

`scutil --get NombreHost`

- Establece nombre del host:

`scutil --set NombreHost {{nombre_host}}`
