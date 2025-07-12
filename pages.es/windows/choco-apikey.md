# choco apikey

> Gestiona claves API para fuentes de Chocolatey.
> Más información: <https://chocolatey.org/docs/commands-apikey>.

- Mostrar una lista de fuentes y sus claves API:

`choco apikey`

- Mostrar una fuente específica y su clave API:

`choco apikey --source "{{url_fuente}}"`

- Establecer una clave API para una fuente:

`choco apikey --source "{{url_fuente}}" --key "{{clave_api}}"`

- Eliminar una clave API para una fuente:

`choco apikey --source "{{url_fuente}}" --remove`
