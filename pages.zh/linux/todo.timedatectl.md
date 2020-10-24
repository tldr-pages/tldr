# timedatectl

> Control the system time and date.

- Check the current system clock time:

`timedatectl`

- Set the local time of the system clock directly:

`timedatectl set-time "{{yyyy-MM-dd hh:mm:ss}}"`

- List available timezones:

`timedatectl list-timezones`

- Set the system timezone:

`timedatectl set-timezone {{timezone}}`

- Enable Network Time Protocol (NTP) synchronization:

`timedatectl set-ntp on`
