# mtr

> Matt's Traceroute: combined traceroute and ping tool.

- Traceroute to a host and continuously ping all intermediary hops:

`mtr {{host}}`

- Disable IP address and host name mapping:

`mtr -n {{host}}`

- Generate output after pinging each hop 10 times:

`mtr -w {{host}}`

- Force IP IPv4 or IPV6:

`mtr -4 {{host}}`
