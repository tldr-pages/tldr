# arping

> Discover and probe hosts in a network using the ARP protocol.
> Useful for MAC addres discovery.

- Ping a host by ARP request packets:

`arping {{host_ip}}`

- Ping a host on a specific interface:

`arping -I {{interface}} {{host_ip}}`

- Ping a host and stop at the first reply:

`arping -f {{host_ip}}`

- Ping a host a specific number of times:

`arping -c {{count}} {{host_ip}}`

- Broadcast ARP request packets to update neighbours' ARP caches:

`arping -U {{your_ip}}`

- Determine whether an IP address is already in use in the network by sending it ARP requests with a 3 seconds timeout:

`arping -D -f -w {{3}} {{target_ip}}`
