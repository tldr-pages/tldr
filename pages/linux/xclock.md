# xclock

> Display the time in analog or digital form.

- Display an analog clock:

`xclock`

- Display a 24 hour digital clock with the hours and minutes fields only:

`xclock -digital -brief`

- Display a digital clock using an strftime format string (see strftime(3)):

`xclock -digital -strftime {{format}}`

- Display a 24 hour digital clock with the hours, minutes and seconds fields that updates every second:

`xclock -digital -strftime '%H:%M:%S' -update 1`

- Display a 12 hour digital clock with the hours and minutes fields only:

`xclock -digital -twelve -brief`
