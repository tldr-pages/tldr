# traceroute

> Print the route packets trace to network host.

- Traceroute to a host:

`traceroute {{host}}`

- Disable IP address and host name mapping:

`traceroute -n {{host}}`

- Specify wait time for response:

`traceroute -w {{0.5}} {{host}}`

- Specify number of queries per hop:

`traceroute -q {{5}} {{host}}`

- Specify size in bytes of probing packet:

`traceroute {{host}} {{42}}`
