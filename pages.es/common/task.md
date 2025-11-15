# task

> Organizador de tareas en la línea de comandos.
> Más información: <https://taskwarrior.org/docs/>.

- Añade una tarea la cual se vence mañana:

`task add {{descripción}} due:{{tomorrow}}`

- Actualiza la prioridad de una tarea:

`task {{id_de_la_tarea}} modify priority:{{H|M|L}}`

- Completa una tarea:

`task {{id_de_la_tarea}} done`

- Elimina una tarea:

`task {{id_de_la_tarea}} delete`

- Lista todas las tareas pendientes:

`task list`

- Lista tareas pendientes que se vencen antes del fin de semana:

`task list due.before:{{eow}}`

- Muestra una gráfica de progreso de tareas, por día:

`task burndown.daily`

- Lista todos los reportes:

`task reports`
