# icalBuddy

> Command-line utility for prinitng events and tasks from the macOS calendar database.
> More information: <https://hasseg.org/icalBuddy/>.

- Show events later today:

`icalBuddy -n -f eventsToday`

- Show uncompleted tasks:

`icalBuddy -f uncompletedTasks`

- Show tasks for the next 3 days:

`icalBuddy -n -f tasksDueBefore:today+3`

- Show events in a time range:

`icalBuddy -f eventsFrom:'{{start date}}' to:'{{end date}}'`

- Show custom event list:

`icalBuddy -f -npn -nc -iep "title,datetime" -ps "| : |" -po "datetime,title" -tf "" -df "%RD" -eed eventsToday+10`
