# choco search

> Busca un paquete local o remoto con Chocolatey.
> Más información: <https://docs.chocolatey.org/en-us/choco/commands/search/>.

- Busca un paquete:

`choco search {{consulta}}`

- Busca un paquete localmente:

`choco search {{consulta}} --local-only`

- Incluir solo coincidencias exactas en los resultados:

`choco search {{consulta}} {{[-e|--exact]}}`

- Confirma automáticamente todos los mensajes:

`choco search {{consulta}} {{[-y|--yes]}}`

- Especifica una fuente personalizada para buscar paquetes:

`choco search {{consulta}} {{[-s|--source]}} {{url_fuente|alias}}`

- Proporciona un nombre de usuario y una contraseña para la autenticación:

`choco search {{consulta}} {{[-u|--user]}} {{nombre_usuario}} {{[-p|--password]}} {{contraseña}}`
