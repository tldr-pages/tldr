# icalBuddy

> Utilidad de línea de comandos para imprimir eventos y tareas desde la base de datos del calendario de macOS.
> Más información: <https://hasseg.org/icalBuddy/>.

- Muestra los eventos de hoy más tarde:

`icalBuddy --includeOnlyEventsFromNowOn eventsToday`

- Muestra tareas no completadas:

`icalBuddy uncompletedTasks`

- Muestra una lista formateada y discriminada de acuerdo al calendario de todos los eventos en el día de hoy:

`icalBuddy --formatOutput --separateByCalendar eventsToday`

- Muestra las tareas para un número determinado de días:

`icalBuddy --includeOnlyEventsFromNowOn "tasksDueBefore:today+{{days}}"`

- Muestra los eventos en un rango de tiempo:

`icalBuddy eventsFrom:{{start_date}} to:{{end_date}}`
