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

- show a route for an IP or subnet

`ip route get {{ip or subnet}}`


- Add a default route for an IP or subnet:

`ip route add default via {{ip or subnet}} dev {{interface}}`


- Show neighbors (ARP table):

`ip neighbour`

- Make an interface up/down:

`ip link set {{interface}} up/down`

- Add/Delete an ip address to an interface:

`ip addr add/del {{ip}}/{{mask}} dev {{interface}}`


- rename interface

``` 
    ip link set dev {{interface}} down
    ip link set {{old interface name}} name {{new interface name}}
    ip link set {{new interface name}} up
```

- delete interface

`ip link delete {{interface}}`

- bring up interface

`ip link set {{interface}} up`

- change MTU (Maximum Transmission Unit) on an interface

`ip link set {{interface}} mtu {{integer}}`

- show statistics/errors for an interface 

`ip link -s link show {{interface}}`

- show all tunnels

`ip tunnel`

- show multicast information for all interfaces

`ip maddr`

- show multicast information for specific interface

`ip maddr show dev {{interface}}`

- add/delete static link-layer multicast address

`ip maddr add/del {{multicast IP}} dev {{interface}}`



