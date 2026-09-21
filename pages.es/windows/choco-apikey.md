# choco apikey

> Gestiona claves API para fuentes de Chocolatey.
> Más información: <https://docs.chocolatey.org/en-us/create/commands/api-key/>.

- Mostra una lista de fuentes y sus claves API:

`choco apikey`

- Mostra una fuente específica y su clave API:

`choco apikey {{[-s|--source]}} "{{url_fuente}}"`

- Establecer una clave API para una fuente:

`choco apikey {{[-s|--source]}} "{{url_fuente}}" {{[-k|--api-key]}} "{{clave_api}}"`

- Elimina una clave API para una fuente:

`choco apikey remove {{[-s|--source]}} "{{url_fuente}}"`
