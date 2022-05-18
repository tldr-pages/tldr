# xfreerdp

> Free Remote Desktop Protocol implementation.
> More information: <https://www.freerdp.com>.

- Connect to a FreeRDP server:

`xfreerdp /u:{{username}} /p:{{password}} /v:{{ip_address}}`

- Connect to a FreeRDP server and activate audio output redirection using `sys:alsa` device:

`xfreerdp /u:{{username}} /p:{{password}} /v:{{ip_address}} /sound:{{sys:alsa}}`

- Connect to a FreeRDP server with dynamic resolution, clipboard redirection and ignore any certificate checks:

`xfreerdp /dynamic-resolution +clipboard /cert:ignore /v:{{ip_address}} /u:{{username}} /p:{{password}}`
