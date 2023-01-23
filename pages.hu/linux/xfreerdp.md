# xfreerdp

> Ingyenes távoli asztali protokoll implementáció. További információ: <https://www.freerdp.com>.

- Csatlakozás egy FreeRDP-kiszolgálóhoz:

`xfreerdp /u:{{username}} /p:{{password}} /v:{{ip_address}}`

- Csatlakozás egy FreeRDP-kiszolgálóhoz és a hangkimenet átirányításának aktiválása a `sys:alsa` eszközzel:

`xfreerdp /u:{{username}} /p:{{password}} /v:{{ip_address}} /sound:{{sys:alsa}}`

- Csatlakozás FreeRDP-kiszolgálóhoz dinamikus felbontással:

`xfreerdp /v:{{ip_address}} /u:{{username}} /p:{{password}} /dynamic-resolution`

- Csatlakozás FreeRDP-kiszolgálóhoz vágólap átirányítással:

`xfreerdp /v:{{ip_address}} /u:{{username}} /p:{{password}} +clipboard`

- Csatlakozás egy FreeRDP-kiszolgálóhoz a tanúsítványok ellenőrzésének figyelmen kívül hagyásával:

`xfreerdp /v:{{ip_address}} /u:{{username}} /p:{{password}} /cert:ignore`
