# icalBuddy

> Utilidad de línea de comandos para imprimir eventos y tareas desde la base de datos del calendario de macOS.
> Más información: <https://hasseg.org/icalBuddy/>.

- Mostrar los eventos de hoy más tarde:

`icalBuddy -n eventsToday`

- Mostrar tareas no completadas:

`icalBuddy uncompletedTasks`

- Mostrar una lista formateada y discriminada de acuerdo al calendario de todos los eventos en el día de hoy:

`icalBuddy -f -sc eventsToday`

- Mostrar las tareas para un número determinado de días:

`icalBuddy -n "tasksDueBefore:today+{{days}}"`

- Mostrar los eventos en un rango de tiempo:

`icalBuddy eventsFrom:{{start_date}} to:{{end_date}}`
