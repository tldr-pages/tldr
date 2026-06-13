# xfreerdp

> Implementació lliure del protocol d'escriptori remot (_Remote Desktop Protocol_).
> Més informació: <https://github.com/FreeRDP/FreeRDP/wiki/CommandLineInterface-(possibly-not-up-to-date,-check-application-help-text-for-most-up-to-date-version)>.

- Connecta amb un servidor FreeRDP:

`xfreerdp /u:{{nom_usuari}} /p:{{contrasenya}} /v:{{direcció_ip}}`

- Connecta amb un servidor FreeRDP i activa la redirecció d'audio fent servir un dispositiu `sys:alsa`:

`xfreerdp /u:{{nom_usuari}} /p:{{contrassenya}} /v:{{direcció_ip}} /sound:{{sys:alsa}}`
