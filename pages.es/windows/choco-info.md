# choco info

> Muestra información detallada sobre un paquete con Chocolatey.
> Más información: <https://chocolatey.org/docs/commands-info>.

- Mostrar información sobre un paquete específico:

`choco info {{paquete}}`

- Mostrar información solo para un paquete local:

`choco info {{paquete}} --local-only`

- Especificar una fuente personalizada para recibir información sobre paquetes:

`choco info {{paquete}} --source {{url_fuente|alias}}`

- Proporcionar un nombre de usuario y una contraseña para la autenticación:

`choco info {{paquete}} --user {{nombre_usuario}} --password {{contraseña}}`
