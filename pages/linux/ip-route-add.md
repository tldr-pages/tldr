# ip route add

> Add a new networking route.
> More information: <https://manned.org/ip-route>.

- Add a default route using gateway forwarding:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{gateway_ip}}`

- Add a default route using `ethX`:

`sudo ip {{[r|route]}} {{[a|add]}} default dev {{ethX}}`

- Add a static route:

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} via {{gateway_ip}} dev {{ethX}}`

- Add a route to a specific routing table:

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} dev {{ethX}} {{[t|table]}} {{ip}}`
