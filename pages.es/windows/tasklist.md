# tasklist

> Muestra una lista de los procesos en ejecución en una máquina local o remota.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/tasklist>.

- Mostrar los procesos en ejecución actualmente:

`tasklist`

- Mostrar procesos en ejecución en un formato de salida específico:

`tasklist /fo {{table|list|csv}}`

- Mostrar procesos que utilizan un archivo `.exe` o `.dll` específico:

`tasklist /m {{patrón_módulo}}`

- Mostrar procesos que se ejecutan en una máquina remota:

`tasklist /s {{nombre_remoto}} /u {{usuario}} /p {{contraseña}}`

- Mostrar servicios usados por cada proceso:

`tasklist /svc`
