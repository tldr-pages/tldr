# taskkill

> Termina un proceso por su ID o nombre.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- Terminar un proceso por su ID:

`taskkill /pid {{id_proceso}}`

- Terminar un proceso por su nombre:

`taskkill /im {{nombre_proceso}}`

- Forzar la terminación de un proceso especificado:

`taskkill /pid {{id_proceso}} /f`

- Terminar un proceso y sus procesos hijos:

`taskkill /im {{nombre_proceso}} /t`

- Terminar un proceso en una máquina remota:

`taskkill /pid {{id_proceso}} /s {{nombre_remoto}}`

- Mostrar información sobre el uso del comando:

`taskkill /?`
