# ntpq

> Query the Network Time Protocol (NTP) daemon.
> More information: <https://manned.org/man/ntpq.1>.

- Start `ntpq` in interactive mode:

`ntpq`

- Print a list of NTP peers:

`ntpq {{[-p|--peers]}}`

- Print a list of NTP peers without resolving hostnames from IP addresses:

`ntpq {{[-n|--numeric]}} {{[-p|--peers]}}`

- Use `ntpq` in debugging mode:

`ntpq {{[-d|--debug-level]}}`

- Print NTP system variables values:

`ntpq {{[-c|--command]}} {{rv}}`
