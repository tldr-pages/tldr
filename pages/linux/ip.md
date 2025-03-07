# ip

> Show/manipulate routing, devices, policy routing and tunnels.
> Some subcommands such as `address` have their own usage documentation.
> More information: <https://www.manned.org/ip.8>.

- List interfaces with detailed info:

`ip {{[a|address]}}`

- List interfaces with brief network layer info:

`ip {{[-br a|-brief address]}}`

- List interfaces with brief link layer info:

`ip {{[-br l|-brief link]}}`

- Display the routing table:

`ip {{[r|route]}}`

- Show neighbors (ARP table):

`ip {{[n|neighbour]}}`

- Make an interface up/down:

`sudo ip {{[l|link]}} {{[s|set]}} {{interface}} {{up|down}}`

- Add/Delete an IP address to an interface:

`sudo ip {{[a|address]}} {{add|delete}} {{ip}}/{{mask}} dev {{interface}}`

- Add a default route:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{ip}} dev {{interface}}`
