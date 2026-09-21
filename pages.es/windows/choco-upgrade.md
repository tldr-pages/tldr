# choco upgrade

> Actualiza uno o más paquetes con Chocolatey.
> Más información: <https://docs.chocolatey.org/en-us/choco/commands/upgrade/>.

- Actualiza uno o más paquetes:

`choco upgrade {{paquete1 paquete2 ...}}`

- Actualiza a una versión específica de un paquete:

`choco upgrade {{paquete}} --version {{versión}}`

- Actualiza todos los paquetes:

`choco upgrade all`

- Actualiza todos excepto los paquetes especificados separados por comas:

`choco upgrade all --except "{{paquete1,paquete2,...}}"`

- Confirma automáticamente todos los mensajes:

`choco upgrade {{paquete}} {{[-y|--yes]}}`

- Especifica una fuente personalizada para recibir paquetes:

`choco upgrade {{paquete}} {{[-s|--source]}} {{url_fuente|alias}}`

- Proporciona un nombre de usuario y una contraseña para la autenticación:

`choco upgrade {{paquete}} {{[-u|--user]}} {{nombre_usuario}} {{[-p|--password]}} {{contraseña}}`
