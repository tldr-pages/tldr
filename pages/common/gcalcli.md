# gcalcli

> Command line tool to interact with Google Calendar.
> First time you run it launches request for API authorization.

- List your events for all your calendars over the next 7 days:

`gcalcli agenda`

- List events from a specific one of your Google Calendars:

`gcalcli --calendar {{calendar name}} agenda`

- Display an ASCII calendar of events by week:

`gcalcli calw`

- Display an ASCII calendar of events for a month:

`gcalcli calm`

- Quick-add an event to your calendar:

`gcalcli --calendar {{calendar name}} quick "{{mm/dd}} {{HH:MM}} {{event name}}"`
