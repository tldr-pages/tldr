# ip neighbour

> Neighbour/ARP tables management IP subcommand.
> More information: <https://manned.org/ip-neighbour>.

- Display the neighbour/ARP table entries:

`ip {{[n|neighbour]}}`

- Remove entries in the neighbour table on device `ethX`:

`sudo ip {{[n|neighbour]}} {{[f|flush]}} dev {{ethX}}`

- Perform a neighbour lookup and return a neighbour entry:

`ip {{[n|neighbour]}} {{[g|get]}} {{lookup_ip}} dev {{ethX}}`

- Add or delete an ARP entry for the neighbour IP address to `ethX`:

`sudo ip {{[n|neighbour]}} {{add|delete}} {{ip_address}} lladdr {{mac_address}} dev {{ethX}} nud reachable`

- Change or replace an ARP entry for the neighbour IP address to `ethX`:

`sudo ip {{[n|neighbour]}} {{change|replace}} {{ip_address}} lladdr {{new_mac_address}} dev {{ethX}}`
