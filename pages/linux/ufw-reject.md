# ufw reject

> Reject traffic through the firewall.
> Similar to `ufw deny`, but sends an ICMP destination-unreachable response instead of silently dropping packets.
> More information: <https://manned.org/ufw>.

- Reject all traffic on a port:

`sudo ufw reject {{port}}`

- Reject traffic for a protocol on a port:

`sudo ufw reject {{port}}/{{protocol}}`

- Reject incoming traffic for a protocol and add a comment for documentation:

`sudo ufw reject in {{protocol}} comment '{{comment}}'`

- Reject all traffic from a source address:

`sudo ufw reject from {{source_address}}`

- Reject all incoming traffic from the subnet 192.168.13.0/24:

`sudo ufw reject from 192.168.13.0/24`

- Reject traffic from a source address to a destination on a specific port and protocol:

`sudo ufw reject from {{source_address}} to {{destination_address}} port {{port}} proto {{protocol}}`

- Reject all incoming traffic on an interface to a destination IP:

`sudo ufw reject in on {{interface}} to {{destination_address}}`
