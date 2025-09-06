# xclock

> Display the time in analog or digital form.
> More information: <https://manned.org/xclock>.

- Display an analog clock:

`xclock`

- Display a 24-hour digital clock with the hour and minute fields only:

`xclock -digital -brief`

- Display a digital clock using an strftime format string (see strftime(3)):

`xclock -digital -strftime {{format}}`

- Display a 24-hour digital clock with the hour, minute and second fields that updates every second:

`xclock -digital -strftime '%H:%M:%S' -update 1`

- Display a 12-hour digital clock with the hour and minute fields only:

`xclock -digital -twelve -brief`
