# ping

> Send ICMP ECHO_REQUEST packets to network hosts.
> See also: `mtr`.
> More information: <https://manned.org/ping>.

- Ping a host with IP `10.0.0.1` (Note: `10.0.0.1` can be shortened to `10.1`):

`ping 10.0.0.1`

- Ping a host only a specific number of times:

`ping -c {{count}} {{host}}`

- Ping host, specifying the interval in seconds between requests (default is 1 second):

`ping -i {{seconds}} {{host}}`

- Ping host without trying to lookup symbolic names for addresses:

`ping -n {{host}}`

- Ping host and ring the bell when a packet is received (if your terminal supports it):

`ping -a {{host}}`

- Also display a message if no response was received:

`ping -O {{host}}`

- Ping a host with specific number of pings, per-packet response timeout (`-W`), and total time limit (`-w`) of the entire ping run:

`ping -c {{count}} -W {{seconds}} -w {{seconds}} {{host}}`
