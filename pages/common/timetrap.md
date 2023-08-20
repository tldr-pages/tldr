# timetrap

> Simple command-line time tracker written in Ruby.
> More information: <https://github.com/samg/timetrap>.

- Create a new timesheet:

`timetrap sheet {{timesheet}}`

- Check in an entry started 5 minutes ago:

`timetrap in --at "{{5 minutes ago}}" {{entry_notes}}`

- Display the current timesheet:

`timetrap display`

- Edit the last entry's end time:

`timetrap edit --end {{time}}`
