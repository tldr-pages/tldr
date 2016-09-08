# date

> Set or display the system date.

- Display the date using the default locale:

`date +"%c"`

- Display the date in UTC and ISO 8601 format:

`date -u +"%Y-%m-%dT%H:%M:%SZ"`

- Display the number of seconds since the unix epoch:

`date +%s`

- Juggle a timestamp representing seconds since the Unix expoch to a date:

`date -j -r 1473305798`
