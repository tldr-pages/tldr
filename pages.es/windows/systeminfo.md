# systeminfo

> Muestra la configuración del sistema operativo para una máquina local o remota.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/systeminfo>.

- Muestra la configuración del sistema para la máquina local:

`systeminfo`

- Muestra la configuración del sistema en un formato de salida especificado:

`systeminfo /fo {{table|list|csv}}`

- Muestra la configuración del sistema para una máquina remota:

`systeminfo /s {{nombre_remoto}} /u {{nombre_de_usuario}} /p {{contraseña}}`

- Muestra la ayuda:

`systeminfo /?`
