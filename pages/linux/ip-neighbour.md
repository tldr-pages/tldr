# ip neighbour

> Neighbour/ARP tables management IP subcommand.
> More information: <https://manned.org/ip-neighbour.8>.

- Display the neighbour/ARP table entries:

`ip {{[n|neighbour]}}`

- Remove entries in the neighbour table on device `eth0`:

`sudo ip {{[n|neighbour]}} {{[f|flush]}} dev {{eth0}}`

- Perform a neighbour lookup and return a neighbour entry:

`ip {{[n|neighbour]}} {{[g|get]}} {{lookup_ip}} dev {{eth0}}`

- Add or delete an ARP entry for the neighbour IP address to `eth0`:

`sudo ip {{[n|neighbour]}} {{add|delete}} {{ip_address}} lladdr {{mac_address}} dev {{eth0}} nud reachable`

- Change or replace an ARP entry for the neighbour IP address to `eth0`:

`sudo ip {{[n|neighbour]}} {{change|replace}} {{ip_address}} lladdr {{new_mac_address}} dev {{eth0}}`
