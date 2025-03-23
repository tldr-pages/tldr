# ip route list

> Display subcommand for IP Routing table management.
> More information: <https://manned.org/ip-route>.

- Display the `main` routing table:

`ip {{[r|route]}} {{[l|list]}}`

- Display the main routing table (same as first example):

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{main|254}}`

- Display the local routing table:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{local|255}}`

- Display all routing tables:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{all|unspec|0}}`

- List routes from a given device only:

`ip {{[r|route]}} {{[l|list]}} dev {{eth0}}`

- List routes within a given scope:

`ip {{[r|route]}} {{[l|list]}} {{[s|scope]}} link`

- Display the routing cache:

`ip {{[r|route]}} {{[l|list]}} {{[c|cache]}}`

- Display only IPv6 or IPv4 routes:

`ip {{-6|-4}} {{[r|route]}}`
