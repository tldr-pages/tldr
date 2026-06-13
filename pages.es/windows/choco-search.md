# choco search

> Busca un paquete local o remoto con Chocolatey.
> Más información: <https://docs.chocolatey.org/en-us/choco/commands/search/>.

- Buscar un paquete:

`choco search {{consulta}}`

- Buscar un paquete localmente:

`choco search {{consulta}} --local-only`

- Incluir solo coincidencias exactas en los resultados:

`choco search {{consulta}} {{[-e|--exact]}}`

- Confirmar automáticamente todos los mensajes:

`choco search {{consulta}} {{[-y|--yes]}}`

- Especificar una fuente personalizada para buscar paquetes:

`choco search {{consulta}} {{[-s|--source]}} {{url_fuente|alias}}`

- Proporcionar un nombre de usuario y una contraseña para la autenticación:

`choco search {{consulta}} {{[-u|--user]}} {{nombre_usuario}} {{[-p|--password]}} {{contraseña}}`
