# timedatectl

> Control the system time and date.
> More information: <https://manned.org/timedatectl>.

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

- Change the hardware clock time standard to localtime:

`timedatectl set-local-rtc 1`
