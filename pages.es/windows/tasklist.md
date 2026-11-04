# tasklist

> Muestra una lista de los procesos en ejecución en una máquina local o remota.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/tasklist>.

- Muestra los procesos en ejecución actualmente:

`tasklist`

- Muestra procesos en ejecución en un formato de salida específico:

`tasklist /fo {{table|list|csv}}`

- Muestra procesos que utilizan un archivo `.exe` o `.dll` específico:

`tasklist /m {{patrón_módulo}}`

- Muestra procesos que se ejecutan en una máquina remota:

`tasklist /s {{nombre_remoto}} /u {{usuario}} /p {{contraseña}}`

- Muestra servicios usados por cada proceso:

`tasklist /svc`
