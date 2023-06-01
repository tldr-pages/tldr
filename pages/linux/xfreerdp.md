# xfreerdp

> Free Remote Desktop Protocol implementation.
> More information: <https://www.freerdp.com>.

- Connect to a FreeRDP server:

`xfreerdp /u:{{username}} /p:{{password}} /v:{{ip_address}}`

- Connect to a FreeRDP server and activate audio output redirection using `sys:alsa` device:

`xfreerdp /u:{{username}} /p:{{password}} /v:{{ip_address}} /sound:{{sys:alsa}}`

- Connect to a FreeRDP server with dynamic resolution:

`xfreerdp /v:{{ip_address}} /u:{{username}} /p:{{password}} /dynamic-resolution`

- Connect to a FreeRDP server with clipboard redirection:

`xfreerdp /v:{{ip_address}} /u:{{username}} /p:{{password}} +clipboard`

- Connect to a FreeRDP server ignoring any certificate checks:

`xfreerdp /v:{{ip_address}} /u:{{username}} /p:{{password}} /cert:ignore`

- Connect to a FreeRDP server with a shared directory:

`xfreerdp /v:{{ip_address}} /u:{{username}} /p:{{password}} /drive:{{path/to/directory}},{{share_name}}`
