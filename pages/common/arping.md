# arping

> Discover and probe hosts in a network using the ARP protocol.
> Useful for MAC address discovery.
> More information: <https://github.com/ThomasHabets/arping>.

- Ping a host by ARP request packets:

`arping {{host_ip}}`

- Ping a host on a specific interface:

`arping -I {{interface}} {{host_ip}}`

- Ping a host and stop at the first reply:

`arping -f {{host_ip}}`

- Ping a host a specific number of times:

`arping -c {{count}} {{host_ip}}`

- Broadcast ARP request packets to update neighbours' ARP caches:

`arping -U {{ip_to_broadcast}}`

- Detect duplicated IP addresses in the network by sending ARP requests with a 3 second timeout:

`arping -D -w {{3}} {{ip_to_check}}`
