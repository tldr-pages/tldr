# ntpq

> Query the Network Time Protocol (NTP) daemon.
More information: <https://www.eecis.udel.edu/~mills/ntp/html/ntpq.html>.

- Start ntpq in interactive mode:

`ntpq --interactive`

- Print list of ntp peers:

`ntpq -p`

- Print list of ntp peers without resolving hostnames from IP addresses:

`ntpq -np`

- Use ntpq in debugging mode:

`ntpq -d`

- Print ntp system variables values:

`ntpq -c rv`
