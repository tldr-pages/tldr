# ping6

> Send ICMP ECHO_REQUEST packets to network hosts via IPv6 address.

- Ping host:

`ping6 {{host}}`

- Ping a host only a specific number of times:

`ping6 -c {{count}} {{host}}`

- Ping host, specifying the interval in seconds between requests (default is 1 second):

`ping6 -i {{seconds}} {{host}}`

- Ping host without trying to lookup symbolic names for addresses:

`ping6 -n {{host}}`

- Ping host and ring the bell when a packet is received (if your terminal supports it):

`ping6 -a {{host}}`
