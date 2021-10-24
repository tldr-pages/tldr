# leave

> Set a reminder for when it's time to leave.
> To remove reminders use `kill $(pidof leave)`.
> More information: <https://www.freebsd.org/cgi/man.cgi?query=leave>.

- Set a reminder at a given time:

`leave {{time_to_leave}}`

- Set a reminder to leave at noon:

`leave {{1200}}`

- Set a reminder in a specific amount of time:

`leave +{{amount_of_time}}`

- Set a reminder to leave in 4 hours and 4 minutes:

`leave +{{0404}}`
