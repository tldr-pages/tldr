# wmic

> Consola interactiva para obtener información detallada sobre los procesos en ejecución.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/wmic>.

- Gramática fundamental:

`wmic {{alias}} {{cláusula_where}} {{cláusula_verb}}`

- Muestra detalles breves sobre los procesos en ejecución actualmente:

`wmic process list brief`

- Muestra detalles completos sobre los procesos en ejecución actualmente:

`wmic process list full`

- Accede a campos específicos como nombre del proceso, ID del proceso e ID del proceso padre:

`wmic process get {{name,processid,parentprocessid}}`

- Muestra información sobre un proceso específico:

`wmic process where {{name="ejemplo.exe"}} list full`

- Muestra campos específicos para un proceso específico:

`wmic process where processid={{pid}} get {{name,commandline}}`

- Termina un proceso:

`wmic process {{pid}} delete`
