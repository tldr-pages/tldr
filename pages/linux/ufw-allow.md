# ufw allow

> Allow traffic through the firewall.
> More information: <https://manned.org/ufw>.

- Allow all traffic on a port:

`sudo ufw allow {{port}}`

- Allow traffic for a protocol on a port:

`sudo ufw allow {{port}}/{{protocol}}`

- Allow incoming traffic for a protocol and add a comment for documentation:

`sudo ufw allow in {{protocol}} comment '{{comment}}'`

- Allow all traffic from a source address:

`sudo ufw allow from {{source_address}}`

- Allow all incoming traffic from the subnet 192.168.13.0/24:

`sudo ufw allow from 192.168.13.0/24`

- Allow TCP traffic from 192.168.1.12 to 192.168.1.100 on port 443:

`sudo ufw allow from 192.168.1.12 to 192.168.1.100 port 443 proto tcp`

- Allow all incoming GRE traffic to 192.168.1.100 on the eth0 interface:

`sudo ufw allow in on eth0 to 192.168.1.100 proto gre`
