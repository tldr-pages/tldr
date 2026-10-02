# ufw deny

> Block traffic through the firewall.
> More information: <https://manned.org/ufw>.

- Deny all traffic on a port:

`sudo ufw deny {{port}}`

- Deny traffic for a protocol on a port:

`sudo ufw deny {{port}}/{{protocol}}`

- Deny incoming traffic for a protocol and add a comment for documentation:

`sudo ufw deny in {{protocol}} comment '{{comment}}'`

- Deny all traffic from a source address:

`sudo ufw deny from {{source_address}}`

- Deny all incoming traffic from the subnet 192.168.13.0/24:

`sudo ufw deny from 192.168.13.0/24`

- Deny UDP traffic from 192.168.1.12 to 192.168.1.100 on port 8080:

`sudo ufw deny from 192.168.1.12 to 192.168.1.100 port 8080 proto udp`

- Deny all incoming IGMP traffic to 192.168.1.100 on the eth0 interface:

`sudo ufw deny in on eth0 to 192.168.1.100 proto igmp`
