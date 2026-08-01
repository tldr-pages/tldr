# ufw allow

> Allow traffic through the firewall.
> More information: <https://manned.org/ufw>.

- Allow all traffic on a port:

`ufw allow {{port}}`

- Allow traffic for a protocol on a port:

`ufw allow {{port}}/{{protocol}}`

- Allow incoming traffic for a protocol and add a comment for documentation:

`ufw allow in {{protocol}} comment '{{comment}}'`

- Allow all traffic from a source address:

`ufw allow from {{source_address}}`

- Allow TCP traffic from 192.168.1.12 to 192.168.1.100 on port 443:

`ufw allow from 192.168.1.12 to 192.168.1.100 port 443 proto tcp`

- Allow all incoming GRE traffic to 192.168.1.100 on the eth0 interface:

`ufw allow in on eth0 to 192.168.1.100 proto gre`
