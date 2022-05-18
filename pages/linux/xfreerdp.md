# xfreerdp

> Free Remote Desktop Protocol implementation.
> More information: <https://www.freerdp.com>.

- Connect to a FreeRDP server:

`xfreerdp /u:{{username}} /p:{{password}} /v:{{ip_address}}`

- Connect to a FreeRDP server and activate audio output redirection using `sys:alsa` device:

`xfreerdp /u:{{username}} /p:{{password}} /v:{{ip_address}} /sound:{{sys:alsa}}`

- Connect to a FreeRDP server with dynamic resolution:

`xfreerdp /dynamic-resolution /v:{{ip_address}} /u:{{username}} /p:{{password}}`

- Connect to a FreeRDP server with clipboard redirection:

`xfreerdp +clipboard /v:{{ip_address}} /u:{{username}} /p:{{password}}`

- Connect to a FreeRDP server ignoring any certificate checks:

`xfreerdp /cert:ignore /v:{{ip_address}} /u:{{username}} /p:{{password}}`
