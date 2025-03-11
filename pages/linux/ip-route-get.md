# ip route get

> Get a single route to a destination and print its contents exactly as the kernel sees it.
> More information: <https://manned.org/ip-route>.

- Print route to a destination:

`ip {{[r|route]}} {{[g|get]}} {{1.1.1.1}}`

- Print route to a destination from a specific source address:

`ip {{[r|route]}} {{[g|get]}} {{destination}} from {{source}}`

- Print route to a destination for packets arriving on a specific interface:

`ip {{[r|route]}} {{[g|get]}} {{destination}} iif {{eth0}}`

- Print route to a destination, forcing output through a specific interface:

`ip {{[r|route]}} {{[g|get]}} {{destination}} oif {{eth1}}`

- Print route to a destination with a specified Type of Service (ToS):

`ip {{[r|route]}} {{[g|get]}} {{destination}} tos {{0x10}}`

- Print route to a destination using a specific VRF (Virtual Routing and Forwarding) instance:

`ip {{[r|route]}} {{[g|get]}} {{destination}} vrf {{myvrf}}`
