# route

> Manually manipulate the routing tables
> Necessitates to be root.

- add a route to a destination through a gateway

`sudo route add 10.0.0.0/8 192.168.1.1`

- run in test mode (does not do anything, just print)

`sudo route -t add 112.1.124.12/32 192.168.1.1`

- remove all routes

`sudo route flush`

- delete a specific route

`sudo route delete 10.0.0.0/24`
