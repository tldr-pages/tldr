# choco info

> Muestra información detallada sobre un paquete con Chocolatey.
> Más información: <https://docs.chocolatey.org/en-us/choco/commands/info/>.

- Mostrar información sobre un paquete específico:

`choco info {{paquete}}`

- Mostrar información solo para un paquete local:

`choco info {{paquete}} {{[-l|--local-only]}}`

- Especificar una fuente personalizada para recibir información sobre paquetes:

`choco info {{paquete}} {{[-s|--source]}} {{url_fuente|alias}}`

- Proporcionar un nombre de usuario y una contraseña para la autenticación:

`choco info {{paquete}} {{[-u|--user]}} {{nombre_usuario}} {{[-p|--password]}} {{contraseña}}`
