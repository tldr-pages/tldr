# xfreerdp3

> Free Remote Desktop Protocol implementation (version 3).
> More information: <https://manned.org/xfreerdp3>.

- Connect to a FreeRDP server:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{ip_address}}`

- Connect to a server in fullscreen mode:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{ip_address}} /f`

- Connect to a server with custom display width and height:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{ip_address}} /w:{{width_in_pixels}} /h:{{height_in_pixels}}`

- Connect to a server with dynamic resolution scaling:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{ip_address}} /dynamic-resolution`

- Connect with clipboard redirection enabled:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{ip_address}} +clipboard`

- Connect to a server with a specific domain:

`xfreerdp3 /u:{{username}} /p:{{password}} /d:{{domain}} /v:{{ip_address}}`

- Connect to a server ignoring certificate checks:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{ip_address}} /cert:ignore`
