# top

> Muestra información dinámica en tiempo real sobre los procesos en ejecución.
> Más información: <https://ss64.com/osx/top.html>.

- Inicia top, todas las opciones están disponibles en la interfaz:

`top`

- Inicia top ordenando los procesos por tamaño de memoria interna (orden por defecto - ID del proceso):

`top -o mem`

- Inicia top ordenando los procesos primero por CPU, luego por tiempo de ejecución:

`top -o cpu -O time`

- Inicia top mostrando sólo los procesos que pertenecen a un usuario determinado:

`top -user {{nombre_usuario}}`

- Obtener ayuda sobre comandos interactivos:

`?`
