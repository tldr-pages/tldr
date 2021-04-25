# ntpq

> Query the Network Time Protocol (NTP) daemon.

- Start ntpq in interactive mode:

`ntpq -i`

- Print list of ntp peers:

`ntpq -p`

- Print list of ntp peers without resolving hostnames from IP addresses:

`ntpq -np`

- Use ntpq in debugging mode:

`ntpq -d`

- Print ntp system variables values:

`ntpq -c rv`
