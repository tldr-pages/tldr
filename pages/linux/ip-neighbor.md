# ip neighbor

> Neighbor/ARP/NDP tables management IP subcommand.
> More information: <https://manned.org/ip-neighbour>.

- Display the neighbor/ARP table entries:

`ip {{[n|neighbor]}}`

- Remove entries in the neighbor table on device `ethX`:

`sudo ip {{[n|neighbor]}} {{[f|flush]}} dev {{ethX}}`

- Perform a neighbor lookup and return a neighbor entry:

`ip {{[n|neighbor]}} {{[g|get]}} {{lookup_ip}} dev {{ethX}}`

- Add or delete an ARP entry for the neighbor IP address to `ethX`:

`sudo ip {{[n|neighbor]}} {{add|delete}} {{ip_address}} lladdr {{mac_address}} dev {{ethX}} nud reachable`

- Change or replace an ARP entry for the neighbor IP address to `ethX`:

`sudo ip {{[n|neighbor]}} {{change|replace}} {{ip_address}} lladdr {{new_mac_address}} dev {{ethX}}`

- Display only IPv6 or IPv4 neighbors:

`ip {{-6|-4}} {{[n|neighbor]}}`
