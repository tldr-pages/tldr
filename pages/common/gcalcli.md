# gcalcli

> Command line tool to interact with Google Calendar.
> Requests Google API authorization upon first launch.
> More information: <https://github.com/insanum/gcalcli>.

- List your events for all your calendars over the next 7 days:

`gcalcli agenda`

- List events from a specific one of your Google Calendars:

`gcalcli --calendar {{calendar_name}} agenda`

- Display an ASCII calendar of events by week:

`gcalcli calw`

- Display an ASCII calendar of events for a month:

`gcalcli calm`

- Quick-add an event to your calendar:

`gcalcli --calendar {{calendar_name}} quick "{{mm/dd}} {{HH:MM}} {{event_name}}"`
