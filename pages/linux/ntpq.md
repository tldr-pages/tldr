# ntpq

> Query the Network Time Protocol (NTP) daemon.
More information: <https://www.eecis.udel.edu/~mills/ntp/html/ntpq.html>.

- Start ntpq in interactive mode:

`ntpq --interactive`

- Print list of ntp peers:

`ntpq --peers`

- Print list of ntp peers without resolving hostnames from IP addresses:

`ntpq --numeric --peers`

- Use ntpq in debugging mode:

`ntpq --debug-level`

- Print ntp system variables values:

`ntpq --command={{rv}}`
