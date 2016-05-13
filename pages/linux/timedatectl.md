# timedatectl

> Control the system time and date.

- To check the current system clock time:

`timedatectl`

- To set the local time of the system clock directly:

`timedatectl set-time {{"yyyy-MM-dd hh:mm:ss"}}`

- To list available timezones:

`timedatectl list-timezones`

- To change timezones:

`timedatectl set-timezone {{timezone}}`

- To enable Network Time Protocol (NTP) syncing:

`timedatectl set-ntp on`
