# ip

> Show / manipulate routing, devices, policy routing and tunnels.
> More information: <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- List interfaces with detailed info:

`ip address`

- List interfaces with brief network layer info:

`ip -brief address`

- List interfaces with brief link layer info:

`ip -brief link`

- Display the routing table:

`ip route`

- Show neighbors (ARP table):

`ip neighbour`

- Make an interface up/down:

`ip link set {{interface}} up/down`

- Add/Delete an ip address to an interface:

`ip addr add/del {{ip}}/{{mask}} dev {{interface}}`

- Add a default route:

`ip route add default via {{ip}} dev {{interface}}`
