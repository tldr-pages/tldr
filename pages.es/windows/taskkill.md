# taskkill

> Termina un proceso por su ID o nombre.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- Termina un proceso por su ID:

`taskkill /pid {{id_proceso}}`

- Termina un proceso por su nombre:

`taskkill /im {{nombre_proceso}}`

- Obliga a la terminación de un proceso especificado:

`taskkill /pid {{id_proceso}} /f`

- Termina un proceso y sus procesos hijos:

`taskkill /im {{nombre_proceso}} /t`

- Termina un proceso en una máquina remota:

`taskkill /pid {{id_proceso}} /s {{nombre_remoto}}`

- Muestra información sobre el uso del comando:

`taskkill /?`
