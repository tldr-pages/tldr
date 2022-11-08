# ip route show

> Display subcommand for IP Routing table management.
> More information: <https://manned.org/ip-route>.

- Display the routing table:

`ip route show`

- Display the main routing table (same as first example):

`ip route show {{main|254}}`

- Display the local routing table:

`ip route show table {{local|255}}`

- Display all routing tables:

`ip route show table {{all|unspec|0}}`

- List routes from a given device only:

`ip route show dev {{eth0}}`

- List routes within a given scope:

`ip route show scope link`

- Display the routing cache:

`ip route show cache`

- Display only IPv6 or IPv4 routes:

`ip {{-6|-4}} route show`
