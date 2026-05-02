# arping

> Discover and probe hosts in a network using the ARP protocol.
> Useful for MAC address discovery.
> More information: <https://manned.org/arping>.

- Ping a host by ARP request packets:

`sudo arping {{host_ip}}`

- Ping a host on a specific [I]nterface:

`sudo arping -I {{interface}} {{host_ip}}`

- Ping a host and [f]inish after the first reply:

`sudo arping -f {{host_ip}}`

- Ping a host a specific number ([c]ount) of times:

`sudo arping -c {{count}} {{host_ip}}`

- Broadcast ARP request packets to update neighbours' ARP caches ([U]nsolicited ARP mode):

`sudo arping -U {{ip_to_broadcast}}`

- [D]etect duplicated IP addresses in the network by sending ARP requests with a 3 second timeout:

`sudo arping -D -w {{3}} {{ip_to_check}}`
