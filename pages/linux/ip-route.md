# ip route

> IP Routing table management subcommand.
> More information: <https://manned.org/ip-route>.

- Display the `main` routing table:

`ip {{[r|route]}}`

- Add a default route using gateway forwarding:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{gateway_ip}}`

- Add a default route using `eth0`:

`sudo ip {{[r|route]}} {{[a|add]}} default dev {{eth0}}`

- Add a static route:

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} via {{gateway_ip}} dev {{eth0}}`

- Delete a static route:

`sudo ip {{[r|route]}} {{[d|delete]}} {{destination_ip}} dev {{eth0}}`

- Change or replace a static route:

`sudo ip {{[r|route]}} {{change|replace}} {{destination_ip}} via {{gateway_ip}} dev {{eth0}}`

- Show which route will be used by the kernel to reach an IP address:

`ip {{[r|route]}} {{[g|get]}} {{destination_ip}}`

- Display a specific routing table:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{table_number}}`
