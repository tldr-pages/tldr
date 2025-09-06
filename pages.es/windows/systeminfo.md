# systeminfo

> Muestra la configuración del sistema operativo para una máquina local o remota.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/systeminfo>.

- Mostrar la configuración del sistema para la máquina local:

`systeminfo`

- Mostrar la configuración del sistema en un formato de salida especificado:

`systeminfo /fo {{table|list|csv}}`

- Mostrar la configuración del sistema para una máquina remota:

`systeminfo /s {{nombre_remoto}} /u {{nombre_de_usuario}} /p {{contraseña}}`

- Mostrar ayuda:

`systeminfo /?`
