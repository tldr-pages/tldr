# ip route show

> IP Routing table management display subcommand.
> More information: <https://manned.org/ip-route>.

- Display the routing table:

`ip route show`

- Display the main routing table (same as first example):

`ip route show {{main|254}}`

- Display the local routing table:

`ip route show table {{local|255}}`

- Display all routing tables:

`ip route show table {{all|unspec|0}}`

- Display the routing cache: 

`ip route show cache`
