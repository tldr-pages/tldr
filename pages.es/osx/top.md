# top

> Muestra información dinámica en tiempo real sobre los procesos en ejecución.
> Más información: <https://keith.github.io/xcode-man-pages/top.1.html>.

- Inicia top, todas las opciones están disponibles en la interfaz:

`top`

- Inicia top ordenando los procesos por tamaño de memoria interna (orden por defecto - ID del proceso):

`top -o mem`

- Inicia top ordenando los procesos primero por CPU, luego por tiempo de ejecución:

`top -o cpu -O time`

- Inicia top mostrando sólo los procesos que pertenecen a un usuario determinado:

`top -user {{nombre_usuario}}`

- Muestra información de ayuda sobre comandos interactivos:

`?`
