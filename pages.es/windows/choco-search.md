# choco search

> Busca un paquete local o remoto con Chocolatey.
> Más información: <https://chocolatey.org/docs/commands-search>.

- Buscar un paquete:

`choco search {{consulta}}`

- Buscar un paquete localmente:

`choco search {{consulta}} --local-only`

- Incluir solo coincidencias exactas en los resultados:

`choco search {{consulta}} --exact`

- Confirmar automáticamente todos los mensajes:

`choco search {{consulta}} --yes`

- Especificar una fuente personalizada para buscar paquetes:

`choco search {{consulta}} --source {{url_fuente|alias}}`

- Proporcionar un nombre de usuario y una contraseña para la autenticación:

`choco search {{consulta}} --user {{nombre_usuario}} --password {{contraseña}}`
