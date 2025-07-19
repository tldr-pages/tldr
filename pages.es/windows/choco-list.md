# choco list

> Muestra una lista de paquetes con Chocolatey.
> Más información: <https://chocolatey.org/docs/commands-list>.

- Mostrar todos los paquetes disponibles:

`choco list`

- Mostrar todos los paquetes instalados localmente:

`choco list --local-only`

- Mostrar una lista que incluya programas locales:

`choco list --include-programs`

- Mostrar solo paquetes aprobados:

`choco list --approved-only`

- Especificar una fuente personalizada para mostrar paquetes:

`choco list --source {{url_fuente|alias}}`

- Proporcionar un nombre de usuario y una contraseña para la autenticación:

`choco list --user {{nombre_usuario}} --password {{contraseña}}`
