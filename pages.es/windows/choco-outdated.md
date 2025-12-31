# choco outdated

> Comprueba paquetes desactualizados con Chocolatey.
> Más información: <https://docs.chocolatey.org/en-us/choco/commands/outdated/>.

- Mostrar una lista de paquetes desactualizados en formato de tabla:

`choco outdated`

- Ignorar paquetes fijados en la salida:

`choco outdated --ignore-pinned`

- Especificar una fuente personalizada para comprobar paquetes:

`choco outdated --source {{url_fuente|alias}}`

- Proporcionar un nombre de usuario y una contraseña para la autenticación:

`choco outdated --user {{nombre_usuario}} --password {{contraseña}}`
