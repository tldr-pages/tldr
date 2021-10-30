# top

> Muestra información dinámica en tiempo real sobre procesos ejecutándose.
> Más información: <https://manned.org/top>.

- Inicia top:

`top`

- No muestra ningún proceso inactivo o zombie:

`top -i`

- Muestra solo procesos pertenecientes a un usuario dado:

`top -u {{usuario}}`

- Ordena procesos por una columna:

`top -o {{nombre_columna}}`

- Muestra los hilos individuales de un proceso dado:

`top -Hp {{id_proceso}}`

- Muestra solo los procesos con un(os) PID(s) dado(s), sepadados por comas. (Normalmente no se conoce el PID de antemano. Este ejemplo lo obtiene del nombre del proceso):

`top -p $(pgrep -d ',' {{nombre_proceso}})`

- Obtiene ayuda acerca de los comandos interactivos:

`?`
