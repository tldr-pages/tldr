# logoff

> Termina una sesión de inicio de sesión.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/logoff>.

- Termina la sesión actual:

`logoff`

- Termina una sesión por su nombre o ID:

`logoff {{nombre_sesión|id_sesión}}`

- Termina una sesión en un servidor específico conectado a través de RDP:

`logoff {{nombre_sesión|id_sesión}} /server:{{nombre_servidor}}`
