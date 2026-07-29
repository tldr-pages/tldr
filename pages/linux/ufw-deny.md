# ufw deny

> Block traffic through the firewall.
> More information: <https://manned.org/ufw>.

- Deny all traffic on a port:

`ufw deny {{port}}`

- Deny traffic for a protocol on a port:

`ufw deny {{port}}/{{protocol}}`

- Deny incoming traffic for a protocol and add a comment for documentation:

`ufw deny in {{protocol}} comment '{{comment}}'`

- Deny all traffic from a source address:

`ufw deny from {{source_address}}`

- Deny UDP traffic from 192.168.1.12 to 192.168.1.100 on port 8080:

`ufw deny from 192.168.1.12 to 192.168.1.100 port 8080 proto udp`

- Deny all incoming IGMP traffic to 192.168.1.100 on the eth0 interface:

`ufw deny in on eth0 to 192.168.1.100 proto igmp`
