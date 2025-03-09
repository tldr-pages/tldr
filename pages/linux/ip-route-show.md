# ip route show

> Display subcommand for IP Routing table management.
> More information: <https://manned.org/ip-route>.

- Display the routing table:

`ip {{[r|route]}} {{[s|show]}}`

- Display the main routing table (same as first example):

`ip {{[r|route]}} {{[s|show]}} {{main|254}}`

- Display the local routing table:

`ip {{[r|route]}} {{[s|show]}} {{[t|table]}} {{local|255}}`

- Display all routing tables:

`ip {{[r|route]}} {{[s|show]}} {{[t|table]}} {{all|unspec|0}}`

- List routes from a given device only:

`ip {{[r|route]}} {{[s|show]}} dev {{eth0}}`

- List routes within a given scope:

`ip {{[r|route]}} {{[s|show]}} {{[s|scope]}} link`

- Display the routing cache:

`ip {{[r|route]}} {{[s|show]}} {{[c|cache]}}`

- Display only IPv6 or IPv4 routes:

`ip {{-6|-4}} {{[r|route]}} {{[s|show]}}`