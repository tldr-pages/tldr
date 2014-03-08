# route

> Manually manipulate the routing tables
> Necessitates to be root.

- add a route to a destination through a gateway

`sudo route add {{dest_ip_address}} {{gateway_address}}`

- add a route to a /24 subnet through a gateway

`sudo route add {{subnet_ip_address}}/24 {{gateway_address}}`

- run in test mode (does not do anything, just print)

`sudo route -t add {{dest_ip_address}}/24 {{gateway_address}}`

- remove all routes

`sudo route flush`

- delete a specific route

`sudo route delete {{dest_ip_address}}/24`
