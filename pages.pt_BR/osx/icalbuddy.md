# icalBuddy

> Utilitário de linha de comando para exibir eventos e tarefas do banco de dados do calendário do macOS.
> Mais informações: <https://hasseg.org/icalBuddy/>.

- Exibe eventos que acontecerão hoje:

`icalBuddy --includeOnlyEventsFromNowOn eventsToday`

- Exibe tarefas incompletas:

`icalBuddy uncompletedTasks`

- Exibe uma lista formatada separada por calendário para todos os eventos de hoje:

`icalBuddy --formatOutput --separateByCalendar eventsToday`

- Exibe tarefas para um determinado número de dias:

`icalBuddy --includeOnlyEventsFromNowOn "tasksDueBefore:today+{{dias}}"`

- Exibe eventos em um intervalo de tempo:

`icalBuddy eventsFrom:{{data_inicial}} to:{{data_final}}`
