# choco upgrade

> Actualiza uno o más paquetes con Chocolatey.
> Más información: <https://chocolatey.org/docs/commands-upgrade>.

- Actualizar uno o más paquetes:

`choco upgrade {{paquete1 paquete2 ...}}`

- Actualizar a una versión específica de un paquete:

`choco upgrade {{paquete}} --version {{versión}}`

- Actualizar todos los paquetes:

`choco upgrade all`

- Actualizar todos excepto los paquetes especificados separados por comas:

`choco upgrade all --except "{{paquete1,paquete2,...}}"`

- Confirmar automáticamente todos los mensajes:

`choco upgrade {{paquete}} --yes`

- Especificar una fuente personalizada para recibir paquetes:

`choco upgrade {{paquete}} --source {{url_fuente|alias}}`

- Proporcionar un nombre de usuario y una contraseña para la autenticación:

`choco upgrade {{paquete}} --user {{nombre_usuario}} --password {{contraseña}}`
