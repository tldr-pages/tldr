# xfreerdp3

> Free Remote Desktop Protocol implementation (version 3).
> More information: <https://manned.org/xfreerdp3>.

- Connect to a FreeRDP server:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}}`

- Connect to a server in fullscreen mode:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}} /f`

- Connect to a server with custom display width and height:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}} /w:{{width_in_pixels}} /h:{{height_in_pixels}}`

- Connect to a server with dynamic resolution scaling:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}} /dynamic-resolution`

- Connect to a server with clipboard redirection:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}} +clipboard`

- Connect to a server with a specific domain:

`xfreerdp3 /u:{{username}} /p:{{password}} /d:{{domain}} /v:{{host}}`

- Connect to a server ignoring certificate checks:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}} /cert:ignore`
