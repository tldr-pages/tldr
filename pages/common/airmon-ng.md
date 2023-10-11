# airmon-ng

> Activate monitor mode on wireless network devices.
> Part of `aircrack-ng`.
> More information: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- List wireless devices and their statuses:

`sudo airmon-ng`

- Turn on monitor mode for a specific device:

`sudo airmon-ng start {{wlan0}}`

- Kill disturbing processes that use wireless devices:

`sudo airmon-ng check kill`

- Turn off monitor mode for a specific network interface:

`sudo airmon-ng stop {{wlan0mon}}`
