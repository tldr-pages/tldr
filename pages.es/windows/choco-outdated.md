# choco outdated

> Comprueba paquetes desactualizados con Chocolatey.
> Más información: <https://docs.chocolatey.org/en-us/choco/commands/outdated/>.

- Muestra una lista de paquetes desactualizados en formato de tabla:

`choco outdated`

- Ignora paquetes fijados en la salida:

`choco outdated --ignore-pinned`

- Especifica una fuente personalizada para comprobar paquetes:

`choco outdated {{[-s|--source]}} {{url_fuente|alias}}`

- Proporciona un nombre de usuario y una contraseña para la autenticación:

`choco outdated {{[-u|--user]}} {{nombre_usuario}} {{[-p|--password]}} {{contraseña}}`
