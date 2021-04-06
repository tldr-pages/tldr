# ip-neighbor

> Neighbor/ARP tables management ip subcommand.
> More information: <https://manned.org/ip-neighbour.8>.

- Display the neighbor/ARP table entries:

`ip neighbor`

- Remove entries in the neighbor table on device `eth0`:

`sudo ip neighbor flush dev {{eth0}}`

- Perform a neighbor lookup and return a neighbor entry:

`ip neighbor get {{lookup_ip}} dev {{eth0}}`

- Add or delete an ARP entry for the neighbour IP address to `eth0`:

`sudo ip neighbor {{add|del}} {{ip_address}} lladdr {{mac_address}} dev {{eth0}} nud reachable`

- Change or replace an ARP entry for the neighbor IP address to `eth0`:

`sudo ip neighbor {{change|replace}} {{ip_address}} lladdr {{new_mac_address}} dev {{eth0}}`
