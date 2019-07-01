# mtr

> Matt's Traceroute: combined traceroute and ping tool.
> More information: <https://bitwizard.nl/mtr>.

- Traceroute to a host and continuously ping all intermediary hops:

`mtr {{host}}`

- Disable IP address and host name mapping:

`mtr -n {{host}}`

- Generate output after pinging each hop 10 times:

`mtr -w {{host}}`

- Force IP IPv4 or IPV6:

`mtr -4 {{host}}`

- Wait for a given time (in seconds) before sending another packet to the same hop:

`mtr -i {{seconds}} {{host}}`
