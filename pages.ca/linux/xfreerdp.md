# xfreerdp

> Implementació lliure del protocol d'escriptori remot (_Remote Desktop Protocol_).
> Més informació: <https://www.freerdp.com>.

- Connecta amb un servidor FreeRDP:

`xfreerdp /u:{{nom_usuari}} /p:{{contrasenya}} /v:{{direcció_ip}}`

- Connecta amb un servidor FreeRDP i activa la redirecció d'audio fent servir un dispositiu `sys:alsa`:

`xfreerdp /u:{{nom_usuari}} /p:{{contrassenya}} /v:{{direcció_ip}} /sound:{{sys:alsa}}`
