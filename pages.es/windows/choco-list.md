# choco list

> Muestra una lista de paquetes con Chocolatey.
> Más información: <https://docs.chocolatey.org/en-us/choco/commands/list/>.

- Mostra todos los paquetes disponibles:

`choco list`

- Mostra todos los paquetes instalados localmente:

`choco list --local-only`

- Mostra una lista que incluya programas locales:

`choco list {{[-i|--include-programs]}}`

- Mostra solo paquetes aprobados:

`choco list --approved-only`

- Especifica una fuente personalizada para Mostra paquetes:

`choco list {{[-s|--source]}} {{url_fuente|alias}}`

- Proporcionar un nombre de usuario y una contraseña para la autenticación:

`choco list --user {{nombre_usuario}} --password {{contraseña}}`
