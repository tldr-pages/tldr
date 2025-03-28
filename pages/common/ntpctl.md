# ntpctl

> Display information about the running instance of OpenNTPD.
> More information: <https://man.openbsd.org/ntpctl>.

- Show all data:

`ntpctl -s {{[a|all]}}`

- Show information about each peer:

`ntpctl -s {{[p|peers]}}`

- Show the status of peers and sensors, and whether the system clock is synced:

`ntpctl -s {{[s|status]}}`

- Show information about each sensor:

`ntpctl -s {{[S|Sensors]}}`
