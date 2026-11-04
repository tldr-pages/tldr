# choco list

> Muestra una lista de paquetes con Chocolatey.
> Más información: <https://docs.chocolatey.org/en-us/choco/commands/list/>.

- Muestra todos los paquetes disponibles:

`choco list`

- Muestra todos los paquetes instalados localmente:

`choco list --local-only`

- Muestra una lista que incluya programas locales:

`choco list {{[-i|--include-programs]}}`

- Muestra solo paquetes aprobados:

`choco list --approved-only`

- Especifica una fuente personalizada para mostrar paquetes:

`choco list {{[-s|--source]}} {{url_fuente|alias}}`

- Proporciona un nombre de usuario y una contraseña para la autenticación:

`choco list --user {{nombre_usuario}} --password {{contraseña}}`
